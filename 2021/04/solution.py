from collections import defaultdict


class Game:
    def __init__(self, file):
        with open(file) as f:
            lines = [line.strip() for line in f]

        self.moves = map(int, lines[0].split(','))

        boards = lines[2:]

        self.nums_to_board_pos = defaultdict(list)
        self.board_state = {}
        num_boards = len(boards) // 6

        for i in range(num_boards):
            self.board_state[i] = [[-1] * 5 for _ in range(5)]
            for j in range(5):
                row = boards[i * 6 + j]
                for k, val in enumerate([int(v) for v in row.split() if v]):
                    self.nums_to_board_pos[val].append((i, j, k))
                    self.board_state[i][j][k] = val

    def mark(self, board, row, col):
        self.board_state[board][row][col] = 0
        if all(self.board_state[board][row][i] == 0 for i in range(5)):
            return True
        if all(self.board_state[board][i][col] == 0 for i in range(5)):
            return True
        # if all(self.board_state[board][i][i] == 0 for i in range(5)):
        #     return True
        # if all(self.board_state[board][i][4-i] == 0 for i in range(5)):
        #     return True
        return False

    def first_board(self):
        for move in self.moves:
            for board, row, col in self.nums_to_board_pos[move]:
                if self.mark(board, row, col):
                    print("Done", board, self.board_state[board])
                    val = sum(sum(row) for row in self.board_state[board])
                    print(val, val*move)
                    return

    def last_board(self):
        used_boards = set()
        for move in self.moves:
            for board, row, col in self.nums_to_board_pos[move]:
                if self.mark(board, row, col):
                    used_boards.add(board)
                    if len(used_boards) == len(self.board_state):
                        print("Done", board)
                        self.print_board(board)
                        val = sum(sum(row) for row in self.board_state[board])
                        print(val, val*move)
                        return

    def print_board(self, board):
        for row in range(5):
            row_str = " ".join([f"{i:02}" for i in self.board_state[board][row]])
            print(row_str)


Game("model_input.txt").first_board()
Game("model_input.txt").last_board()
Game("input.txt").first_board()
Game("input.txt").last_board()


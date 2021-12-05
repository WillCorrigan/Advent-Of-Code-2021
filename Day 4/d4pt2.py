from collections import Counter

class Board:
    def __init__(self, index, lines):
        self.index = index
        self.lines = lines
        self.winner = False
        self.checked_as_winner = False

    def mark_winning_numbers(self, bingo_number):
        if self.winner == True and self.checked_as_winner == False:
            self.checked_as_winner = True
            return
        if self.checked_as_winner:
            return
        for l_index, line in enumerate(self.lines):
            for n_index, number in enumerate(line):
                if number == bingo_number:
                    self.lines[l_index][n_index] = 'marked'
        self.mark_if_winner()
        return self.winner

    def mark_if_winner(self):
        tmp_row = [Counter(x) for x in self.lines]
        tmp_column = [Counter(x) for x in zip(*self.lines)]

        for indx, val in enumerate(tmp_row):
            if val.most_common()[0][1] == 5:
                self.winner = True
                return

        for indx, val in enumerate(tmp_column):
            if val.most_common()[0][1] == 5:
                self.winner = True
                return
        self.winner = False
        return
        
filename = "data.txt"

boards_lst = []
numbers = None
tmp_boards = []


with open(filename) as f:
    content = f.readlines()

    for index, line in enumerate(content):
        line = line.strip().split(",")

        if index == 0:
            numbers = [x for x in line]
            continue

        if line[0] == "" and index != 1:
            boards_lst.append(tmp_boards)
            tmp_boards = []
            continue

        elif index != 1:
            tmp_boards.append(line[0].split())

board_objects = [Board(index, board) for index, board in enumerate(boards_lst)]

object_total = len(board_objects)
total_winners = 0

def process(n_index, bingo_number):
    global total_winners
    for b_index, board in enumerate(board_objects):
        board.mark_winning_numbers(bingo_number)
        if board.winner == True and board.checked_as_winner == False:
            total_winners = total_winners + 1
            print("Winning board is: " + str(b_index))
        if total_winners == object_total - 1:
            losing_board = [x for x in board_objects if x.winner == False][0]
            for n in numbers[n_index:]:
                losing_board.mark_winning_numbers(n)
                if losing_board.winner:
                    print("Bingo Number is: " + n)
                    winning_lines = losing_board.lines
                    print(winning_lines)
                    remaining_numbers_total = sum([int(i) for lst in winning_lines for i in lst if i != "marked"])
                    print("Total Numbers Added: " + str(remaining_numbers_total))
                    print("Answer is: " + str(int(n) * int(remaining_numbers_total)))
                    return True
        
                
for index, value in enumerate(numbers):
    if process(index, value):
        break
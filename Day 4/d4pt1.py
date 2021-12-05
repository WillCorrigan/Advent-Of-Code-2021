from collections import Counter

filename = "data.txt"
with open(filename) as f:
    content = f.readlines()

    numbers = None
    tmp_boards = []
    boards_lst = []

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


def mark_numbers(bingo_number):
    for b_index, board in enumerate(boards_lst):
        for l_index, line in enumerate(board):
            for n_index, number in enumerate(line):
                if number == bingo_number:
                    boards_lst[b_index][l_index][n_index] = 'marked'
        if check_if_winner(boards_lst[b_index], b_index, bingo_number):
            return True
    return False

def check_if_winner(board, board_index, bingo_number):
    tmp_row = [Counter(x) for x in board]
    tmp_column = [Counter(x) for x in zip(*board)]

    for indx, val in enumerate(tmp_row):
        if val.most_common()[0][1] == 5:
            print("winner is board: " + str(board_index))
            print("total of unmarked numbers is: " + str(sum([int(i) for list in board for i in list if i != "marked"])))
            print("total multiplied by winning number is: " + str(sum([int(i) for list in board for i in list if i != "marked"]) * int(bingo_number)))
            return True

    for indx, val in enumerate(tmp_column):
        if val.most_common()[0][1] == 5:
            print("winner is board: " + str(board_index))
            print("total of unmarked numbers is: " + str(sum([int(i) for list in board for i in list if i != "marked"])))
            print("total multiplied by winning number is: " + str(sum([int(i) for list in board for i in list if i != "marked"]) * int(bingo_number)))
            return True
            
    return False
        
for i in numbers:
    if mark_numbers(i):
        break
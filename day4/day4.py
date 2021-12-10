import math

bingo_boards = []
with open('day4_input.txt') as f:
    input = list(map(int,f.readline().strip().split(',')))
    while f.readline():
        bingo_board = []
        for _ in range(5):
            bingo_board.extend(list(map(int,f.readline().strip().split())))
        bingo_boards.append((bingo_board,[False]*25))

boards_won = [False for _ in bingo_boards]
boards_score = []

done = False
for i in input:
    for j,(board, mark) in enumerate(bingo_boards):
        if i in board:
            idx = board.index(i)
            mark[idx] = True
            if all(mark[slice(start:=5*math.floor(idx/5),start+5)]) or all(mark[slice(idx%5,25,5)]):
                boards_score.append(i*sum(board[i] for i, m in enumerate(mark) if not m))
                boards_won[j] = True
                if all(boards_won):
                    done = True
                    break
    if done:
        break

print(boards_score[0])
print(boards_score[-1])
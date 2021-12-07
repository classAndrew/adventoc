with open("input.txt") as f:
    data = f.read().split('\n\n')

callout = [int(x) for x in data[0].split(',')]

boards = []
for board in data[1:]:
    kmap = {}
    board = board.split('\n')
    for r in range(len(board)):
        col = [x for x in board[r].split(' ') if x]
        for c in range(len(col)):
            kmap[int(col[c])] = (r, c)
    
    # len(rows) + len(cols) 
    boards.append([[0]*(5+5), kmap])
    
def check_bingo(state, rows, cols):
    return any(x == rows or x == cols for x in state)
    
# winner = -1
# last_callout = -1
# for n in callout:
#     done = False
#     for i in range(len(boards)):
#         state, b = boards[i]
#         rows, cols = 5, 5

#         if n in b:
#             r, c = b[n]
#             state[r] += 1
#             state[rows+c] += 1

#             del b[n]

#         if check_bingo(state, rows, cols):
#             winner = i
#             last_callout = n

#     if win_cnt == len(boards):
#         break

# s = sum(k for k in boards[winner][1])

# print(s*last_callout)

winner = -1
win_cnt = 0
last_callout = -1
won = set()
for n in callout:
    done = False
    for i in range(len(boards)):
        if i in won: continue
        state, b = boards[i]
        rows, cols = 5, 5

        if n in b:
            r, c = b[n]
            state[r] += 1
            state[rows+c] += 1

            del b[n]

        if check_bingo(state, rows, cols):
            won.add(i)
            winner = i
            last_callout = n
            win_cnt += 1

    if win_cnt == len(boards):
        break

s = sum(k for k in boards[winner][1])

print(boards[winner])
print(winner, s*last_callout)
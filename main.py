# 再帰処理が重すぎて実行できない.

initTurn=2
initBoard=[
  0,0,1,0,0,
  0,0,2,0,0,
  0,0,1,0,0,
  0,0,2,0,0,
  0,0,1,0,0
]


def runProgram():
  checkList=[]

  for i in range(5):
    for j in range(5):
      if 5*j+i==0:
        checkList.append(main(initTurn, 5*j+i, initBoard))
        break

  match judgeFromList(checkList, initTurn):
    case 0:
      result="引き分け"
    case 1:
      result="先手必勝"
    case 2:
      result="後手必勝"

  print(result)
  return


def main(turn, index, _board):
  board=_board[:]
  board[index]=turn
  nextTurn=turn-1+2*(turn%2)
  checkList=[]

  if judge(index, board):
    return turn

  for i in range(5):
    for j in range(5):
      if 5*j+i==0:
        checkList.append(main(nextTurn, 5*j+i, board))
        break

  if len(checkList)==0:
    return 0

  return judgeFromList(checkList, nextTurn)


def judgeFromList(checkList, turn):
  if turn in checkList:
    return turn
  elif 0 in checkList:
    return 0
  else:
    return checkList[0]


def judge(index, board):
  for i in range(len(ref[index])):
    if ((board[ref[index][i][0]]==board[index])&
        (board[ref[index][i][1]]==board[index])&
        (board[ref[index][i][2]]==board[index])):
      return True
  return False


ref=[
[[1,2,3],[5,10,15],[6,12,18]],         # 0
[[0,2,3],[2,3,4],[6,11,16],[7,13,19]], # 1
[[0,1,3],[1,3,4],[7,12,17]],           # 2
[[0,1,2],[1,2,4],[8,13,18],[7,11,15]], # 3
[[1,2,3],[9,14,19],[8,12,16]],         # 4

[[0,10,15],[10,15,20],[6,7,8],[11,17,23]],                   # 5
[[5,7,8],[7,8,9],[1,11,16],[11,16,21],[0,12,18],[12,18,24]], # 6
[[5,6,8],[6,8,9],[2,12,17],[12,17,22],[1,13,19],[3,11,15]],  # 7
[[5,6,7],[6,7,9],[3,13,18],[13,18,23],[4,12,16],[12,16,20]], # 8
[[6,7,8],[4,14,19],[14,19,24],[13,17,21]],                   # 9

[[0,5,15],[5,15,20],[11,12,13]],                                                  # 10
[[10,12,13],[12,13,14],[1,6,16],[6,16,21],[3,7,15],[5,17,23]],                    # 11
[[10,11,13],[11,13,14],[2,7,17],[7,17,22],[0,6,18],[6,18,24],[4,8,16],[8,16,20]], # 12
[[10,11,12],[11,12,14],[3,8,18],[8,18,23],[1,7,19],[9,17,21]],                    # 13
[[11,12,13],[4,9,19],[9,19,24]],                                                  # 14

[[0,5,10],[5,10,20],[16,17,18],[3,7,11]],                       # 15
[[15,17,18],[17,18,19],[1,6,11],[6,11,21],[4,8,12],[8,12,20]],  # 16
[[15,16,18],[16,18,19],[2,7,12],[7,12,22],[5,11,23],[9,13,21]], # 17
[[15,16,17],[16,17,19],[3,8,13],[8,13,23],[0,6,12],[6,12,24]],  # 18
[[16,17,18],[4,9,14],[9,14,24],[1,7,13]],                       # 19

[[5,10,15],[21,22,23],[8,12,16]],            # 20
[[20,22,23],[22,23,24],[6,11,16],[9,13,17]], # 21
[[20,21,23],[21,23,24],[7,12,17]],           # 22
[[20,21,22],[21,22,24],[8,13,18],[5,11,17]], # 23
[[21,22,23],[9,14,19],[6,12,18]]             # 24
]


runProgram()

# opponents moves => A: 'Rock', B: 'Paper', C: 'Scissors'
# own move => X: ('Rock', 1), Y: ('Paper', 2), Z: ('Scissors', 3)

opp_moves = {
  'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'
}

own_moves = {
  'X': ('Rock', 1), 'Y': ('Paper', 2), 'Z': ('Scissors', 3)
}

def checkWin(opp_move, own_move):
  if opp_moves[opp_move] == own_moves[own_move][0]:
    return 3
  elif opp_moves[opp_move] == 'Rock' and own_moves[own_move][0] == 'Scissors':
    return 0
  elif opp_moves[opp_move] == 'Paper' and own_moves[own_move][0] == 'Rock':
    return 0
  elif opp_moves[opp_move] == 'Scissors' and own_moves[own_move][0] == 'Paper':
    return 0
  else:
    return 6

output = 0

while True:
  try:
    line = input().split()

    if line[0] != 'stop':
      # do something
      output += checkWin(line[0], line[1])
      output += own_moves[line[1]][1]

    else:
      print(output)
      break

  except EOFError:
    break
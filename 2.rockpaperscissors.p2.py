# Key the inputs in the terminal
# type stop to output the final score
opp_moves = {
  'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'
}

own_moves = {
  'Rock': 1, 'Paper': 2, 'Scissors': 3
}

tactic = {
  'X': ('Lose', 0), 
  'Y': ('Draw', 3), 
  'Z': ('Win', 6)
}

def checkWin(opp_move, own_move): # might wanna change the if-else conditions to hash mapping to reduce complexity
  if tactic[own_move][0] == 'Draw':
    return own_moves[opp_moves[opp_move]]
  elif tactic[own_move][0] == 'Win':
    if opp_moves[opp_move] == 'Rock':
      return own_moves['Paper']
    elif opp_moves[opp_move] == 'Paper':
      return own_moves['Scissors']
    else:
      return own_moves['Rock']
  else:
    if opp_moves[opp_move] == 'Paper':
      return own_moves['Rock']
    elif opp_moves[opp_move] == 'Scissors':
      return own_moves['Paper']
    else:
      return own_moves['Scissors']

output = 0

while True:
  try:
    line = input().split()

    if line[0] != 'stop':
      # do something
      output += checkWin(line[0], line[1])
      output += tactic[line[1]][1]

    else:
      print(output)
      break

  except EOFError:
    break
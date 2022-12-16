''' LIBRARIES'''
from collections import deque # using a deque for faster popleft & appendleft, alternatively - can cosisder using a reversed python list and just pop and append at the back of the list

''' Initialize global variable'''
CRATE_STACK = {} # to store the crate structure

''' Functions '''
def addDict(key, value): # to store the value into the crate stack structure
  if key not in CRATE_STACK:
    CRATE_STACK[key] = deque(value)
  else:
    CRATE_STACK[key].append(value)

def convertLine(line): # to convert line to the crate stack structure
  for i in range(len(line)):
    if line[i].isalpha():
      addDict(i+1, line[i])

def convertMove(move): # to convert line to the apropriate move & move the crate over
  numOfMoves, crate1, crate2 = int(move[1]), int(move[3]), int(move[5])
  if numOfMoves == 1:
    removed_crate = CRATE_STACK[crate1].popleft()
    CRATE_STACK[crate2].appendleft(removed_crate)
  else:
    temp_stack = deque()
    for _ in range(numOfMoves):
      removed_crate = CRATE_STACK[crate1].popleft()
      temp_stack.append(removed_crate)
    
    while temp_stack:
      CRATE_STACK[crate2].appendleft(temp_stack.pop()) # takes out last item from temp_stack and add it to the left of crate2

def extractTopItemPerStack(stack): # to extract the top item per stack & return a string of all the top items
  output = ''
  for k, v in sorted(stack.items()):
    output += v.popleft()
  return output
      
''' MAIN FUNCTION '''
with open('example.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:

      if line != '\n' and line[0:4] != 'move': # store in crate stack
        convertLine(line[1::4])

      elif line == '\n': # skip the line
        continue

      else: # conduct the moves
        convertMove(line.split())
    
    print(extractTopItemPerStack(CRATE_STACK))
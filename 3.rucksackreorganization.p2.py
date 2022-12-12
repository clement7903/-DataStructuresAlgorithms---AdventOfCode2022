''' Initialize global variable'''
OUTPUT = 0

''' Functions '''
def checkPriority(char):

  if char == char.lower():
    return (ord(char)%97 + 1)
  else:
    return (ord(char) - 38)

def checkStop(line):
  if line == 'stop':
    print(OUTPUT)
    return


while True:
  try:

    bags = []

    # For each group 
    for _ in range(3):
      line = input() 

      checkStop(line) # checks for stop word

      # For each bag
      bag = set() 
      for i in range(len(line)):
        bag.add(line[i])
      
      bags.append(bag)
    
    if bags:
        
      union_set = bags[0].intersection(bags[1],bags[2])

      if union_set:
        
        for item in union_set:
          OUTPUT += checkPriority(item)

  except EOFError:
    break
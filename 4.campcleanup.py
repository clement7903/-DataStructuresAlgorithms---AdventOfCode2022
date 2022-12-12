''' Initialize global variable'''
OUTPUT = 0

''' Functions '''
def checkContain(pairs):

  elf1, elf2 = pairs[0].split('-'), pairs[1].split('-')

  if (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]) or (elf2[0] >= elf1[0] and elf2[1] <= elf1[1]): # if either elf is within range
    return 1
  
  return 0

def checkStop(line):

  if line == 'stop':
    print(OUTPUT)
    return True
  
  return False

''' MAIN FUNCTION '''
while True:
  try:
    line = input()

    if checkStop(line) == False:

      pairs = line.split(',')
      
      OUTPUT += checkContain(pairs)
    
    else:
      break

  except EOFError:
    break
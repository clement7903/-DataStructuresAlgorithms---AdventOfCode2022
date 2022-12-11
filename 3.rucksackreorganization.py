output = 0
def checkPriority(char):

  if char == char.lower():
    return (ord(char)%97 + 1)
  else:
    return (ord(char) - 38)

while True:
  try:
    line = input()

    if line == 'stop':
      print(output)
      break

    # continue here
    first_half, second_half = line[:len(line)//2], line[len(line)//2:]

    first_set, second_set = set(), set()

    for i in range(len(line)//2):
      first_set.add(first_half[i])
      second_set.add(second_half[i])
    
    union_set = first_set.intersection(second_set)

    if union_set:
      
      for item in union_set:
        output += checkPriority(item)

  except EOFError:
    break
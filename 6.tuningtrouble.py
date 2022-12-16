# checks for repeated character in substring
def checkRepeatedChar(substring): 
  present_char = set()
  for char in substring:
    if char not in present_char:
      present_char.add(char)
    else:
      return True
  return False

#returns substring of 4 characters 
def checkMarker(string):
  for i in range(len(string)-4):
    sub_string = string[i:i+4]
    if not checkRepeatedChar(sub_string):
      return i + 4
  return None

with open('example.txt', 'r') as f:
    lines = f.readlines()
    print(checkMarker(lines[0]))
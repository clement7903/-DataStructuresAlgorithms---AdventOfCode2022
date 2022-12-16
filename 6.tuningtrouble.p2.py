# CONSTANTS
CHAR_NUM = 14

# checks for repeated character in substring
def checkRepeatedChar(substring): 
  present_char = set()
  for char in substring:
    if char not in present_char:
      present_char.add(char)
    else:
      return True
  return False

#returns substring of CHAR_NUM characters 
def checkMarker(string):
  for i in range(len(string)-CHAR_NUM):
    sub_string = string[i:i+CHAR_NUM]
    if not checkRepeatedChar(sub_string):
      return i + CHAR_NUM
  return None

with open('example.txt', 'r') as f:
    lines = f.readlines()
    print(checkMarker(lines[0]))
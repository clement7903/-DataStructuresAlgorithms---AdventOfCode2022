from heapq import heappop, heappush

lst = []
counter = 1 
total = 0

while True:
  try:
    line = input()
    
    if not line:
      heappush(lst, (-total, counter))
      total = 0
    
    elif line == 'STOP':
      top3 = 0
      for _ in range(3):
        highest = heappop(lst)
        top3 += -highest[0]
      print(top3)
    
    else:
      total += int(line)
    
  except EOFError:
    break
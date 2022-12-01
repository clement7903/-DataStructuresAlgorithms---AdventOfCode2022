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
      for _ in range(3):
        highest = heappop(lst)
        print(-highest[0])
    
    else:
      total += int(line)
    
  except EOFError:
    break

  



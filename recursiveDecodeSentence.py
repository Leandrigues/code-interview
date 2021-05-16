# DailyCoding 7 (recursive/DP try)
def recursiveSolution(s): # O(2^n)
  if len(s) <= 1:
    return 1
  if s[0] == 0:
    return 0
  total = 0
  if int(s[:2]) <= 26:
    total += recursiveSolution(s[1:]) + recursiveSolution(s[2:])
  else:
    total += recursiveSolution(s[1:])

  return total

def solution(s):
  cache = [0]*(len(s) + 1)
  if int(s[0]) != 0:
    cache[0] = 1
  if int(s[1]) != 0:
    cache[1] = 1

  for i in range(1, len(s)):
    if int(s[i-1:i+1]) <= 26:
      # print(f'{s[i-1:i+1]} <= 26')
      cache[i+1] = cache[i] + cache[i-1]
    else:
      # print(f'{s[i-1:i+1]} > 26')
      cache[i+1] = cache[i]

  return cache[-1]

print("Recursive:", recursiveSolution(s))
print("DP:", solution(s))


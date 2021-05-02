# GeeksForGeeks Dynamic Programming
def solution(n):
  cache = [0] * (n + 1)
  cache[0] = 1
  for i in range(1, n + 1):
    for j in [1, 3, 5]:
      if i - j >= 0:
        cache[i] += cache[i-j]

  return cache[n]

print(solution(7))

# DailyCoding 40
def nonRepeatedInteger(arr):
  resultMap = {}

  for item in arr:
    if item in resultMap:
      resultMap[item] += 1
    else:
      resultMap[item] = 1

  for key in resultMap:
    if resultMap[key] != 3:
      return key
result = nonRepeatedInteger([6, 1, 3, 3, 3, 6, 6])
print(result)

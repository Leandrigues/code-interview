# DailyCoding
def subsets(arr):
  if not arr:
      return [[]]
  result = subsets(arr[1:])
  return result + [subset + [arr[0]] for subset in result]

print(subsets(['a', 'b']))

subsets([a, b])

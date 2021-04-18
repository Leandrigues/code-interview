class Node:
  def __init__(self, data, isEnd = False, left=None, right=None, mid=None):
    self.data = data
    self.left = left
    self.right = right
    self.mid = mid
    self.isEnd = isEnd

class TST:
  def __init__(self, initWord):
    self.root = None
    self.root = self.put(initWord)

  def putWord(self, root, word, d):
    char = word[d]
    if root is None:
      root = Node(char)
    if char < root.data:
      root.left = self.putWord(root.left, word, d)
    elif char > root.data:
      root.right = self.putWord(root.right, word, d)
    elif d < len(word) - 1:
      root.mid = self.putWord(root.mid, word, d + 1)
    else:
      root.isEnd = True
    return root

  def put(self, word):
    return self.putWord(self.root, word, 0)

  def getWord(self, root, word, d):
    if root is None:
      return
    char = word[d]
    if char < root.data: return self.getWord(root.left, word, d)
    elif char > root.data: return self.getWord(root.right, word, d)
    elif d < len(word) - 1: return self.getWord(root.mid, word, d + 1)
    else: return root

  def get(self, word):
    node = self.getWord(self.root, word, 0)
    # if node is None or not node.isEnd:
      # print(f"{word} not found.")
    # else:
      # print(f"{word} is in TST")
    return node

  def prefixes(self, prefix):
    root = self.get(prefix)
    arr = []
    if root.isEnd:
      arr.append(prefix)
    return self.searchAllByPrefix(root.mid, arr, prefix)

  def searchAllByPrefix(self, root, arr, prefix):
    if root is None:
      return
    self.searchAllByPrefix(root.left, arr, prefix)
    if root.isEnd:
      arr.append(prefix + root.data)
    self.searchAllByPrefix(root.mid, arr, prefix + root.data)
    self.searchAllByPrefix(root.right, arr, prefix)

def solution(set, query):
  tst = TST(set[0])
  for word in set[1:]:
    tst.put(word)
  result = tst.prefixes(query)
  return result

print(solution(["dog", "deer", "deal"], "de"))

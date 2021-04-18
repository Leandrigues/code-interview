# Daily Coding 8
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isUnival(root, val):
  if root is None:
    return True
  if root.val == val:
    return isUnival(root.left, val) and isUnival(root.right, val)
  return False
def countUnival(root):
  countUnival.i = 0

  def countUnivalHelper(root): 
    # O(n^2)
    if root is None:
      return
    if isUnival(root, root.val):
      countUnival.i += 1
    countUnivalHelper(root.left)
    countUnivalHelper(root.right)
  countUnivalHelper(root)

  return countUnival.i
root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
# root = Node(1, Node(1), Node(1))
print(countUnival(root))
# print(isUnival(root, root.val))
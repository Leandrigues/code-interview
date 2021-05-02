# Daily Coding 36
class Node:
  def __init__(self, val, left=None, right=None):
    self.left = left
    self.right = right
    self.val = val

def secondLargest(root):
  stack = [root.val, root.val]
  def helper(root, stack):
    if root is None:
      return
    if root.val > stack[-1]:
      print(f"I. {root.val} >= {stack[-1]}", end="")
      # stack = [stack[-1], root.val]
      stack[0] = stack[-1]
      stack[1] = root.val
    elif root.val >= stack[0] and root.val < stack[-1]:
      stack[0] = root.val
    else:
    helper(root.left, stack)
    helper(root.right, stack)
    return stack

  stack = helper(root, stack)

a = Node(3)
b = Node(2, a)
c = Node(4, None, b)
d = Node(2)
root = Node(0, d, c)
secondLargest(root)
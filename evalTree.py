# DailyCoding 50
class Node:
  def __init__(self, val=None, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def evalTree(root):
  if type(root.val) is int:
    return root.val
  if root.val == '*':
    return evalTree(root.left) * evalTree(root.right)
  if root.val == '+':
    return evalTree(root.left) + evalTree(root.right)

a = Node(3)
b = Node(2)
c = Node(4)
d = Node(5)
e = Node('+', a, b)
f = Node('+', c, d)
g = Node('*', e, f)

print(evalTree(g))
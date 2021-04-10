# Daily Coding 3
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
  if root == None:
    return None
  elif root.left == None and root.right == None:
    return f'{root.val} {root.left} {root.right}'
  else:
    left = serialize(root.left)
    right = serialize(root.right)

    return f'({root.val} ({left}) ({right}))'

def deserialize(s):
  def helper():
    val = next(vals)

    val = val.replace(')', "")
    val = val.replace('(', "")
    if val == 'None':
      return None

    node = Node(val, helper(), helper())
    return node
  vals = iter(s.split())
  return helper()


node = Node('root', Node('left', Node('left.left')), Node('right'))
serialized = serialize(node)
deserialized = deserialize(serialized)

assert deserialize(serialize(node)).left.left.val == 'left.left'
print("SERIALIZED:", serialized)
print("DESERIALIZED: ", serialize(deserialized))


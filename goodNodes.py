class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.ans = 0

    def goodNodes(self, root):
        def aux(root, current_max):
            if not root:
                return

            if root.val >= current_max:
                self.ans += 1
                current_max = root.val

            aux(root.left, current_max)
            aux(root.right, current_max)

        aux(root, -1000)
        return self.ans

root = TreeNode(3)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.right = TreeNode(4)
root.right.right = TreeNode(5)
root.right.left = TreeNode(1)

ans = Solution().goodNodes(root)
print(ans)
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
    if root is None:
        return
    binaryTreePaths(root.left)
    binaryTreePaths(root.right)
    print(root.val)

Node6 = TreeNode(val=6)
Node3 = TreeNode(val=3, left=Node6)
Node5 = TreeNode(val=5)
Node2 = TreeNode(val=2, left=Node5)
Node1 = TreeNode(val=1, left=Node2, right=Node3)

binaryTreePaths(Node1)
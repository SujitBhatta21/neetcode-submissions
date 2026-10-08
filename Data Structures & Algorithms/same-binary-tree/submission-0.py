# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def stringyfy(root):
            if root is None:
                return "#"
            return "" + str(root.val) + stringyfy(root.left) + stringyfy(root.right)
        
        s1 = stringyfy(p)
        s2 = stringyfy(q)
        print(f"s1: {s1} s2: {s2}")
        if s1 == s2:
            return True
        return False
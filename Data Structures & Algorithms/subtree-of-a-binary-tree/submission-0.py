# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def stringyfy(root):
            if root is None:
                return "#"
            return "" + str(root.val) + stringyfy(root.left) + stringyfy(root.right)
        
        s1 = stringyfy(root)
        s2 = stringyfy(subRoot)
        print(f"s1: {s1} s2: {s2}")
        if s2 in s1:
            return True
        return False
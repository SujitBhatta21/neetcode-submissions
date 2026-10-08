# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Doing breadth first search
        if root is None:
            return []
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            level = []
            N = len(q)
            for i in range(N):
                curr_node = q.popleft()
                level.append(curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            res.append(level)

        return res


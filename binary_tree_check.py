# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
class Solution:
    def isValidBST(self, root):
        
        res, ans = [-float('inf')], True
        
        def recur(root):
            nonlocal res, ans
            if not root:
                return
            recur(root.left)
            if root.val <= res[-1]:
                ans &= False
            res.append(root.val)
            recur(root.right)
            
        recur(root)
        return ans
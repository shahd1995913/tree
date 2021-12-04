# Given the root node of a binary search 
# tree and two integers low and high, return the sum of 
# values of all nodes with a value in the inclusive range [low, high].

class Solution(object):
	def rangeSumBST(self, root, low, high):
        if not root: return 0
        if root.val > high: return self.rangeSumBST(root.left,low,high)
        if root.val < low: return self.rangeSumBST(root.right,low,high)
        return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high) 
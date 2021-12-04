# Given the root of a binary tree, return the sum of values of its deepest leaves.
class Solution(object):
    def deepestLeavesSum(self, root):

        def maxdepth(root):

            if not root:
                return 0
            else:
                return 1 + max(maxdepth(root.left), maxdepth(root.right)) 

        level = maxdepth(root)

        arr = []

        def findsum(root, level):

            if not root:

                return 0
            if level == 1:

                arr.append(root.val)
            else:

                findsum(root.left, level-1)

                findsum(root.right, level-1)

        findsum(root, level)

        return sum(arr)
        
# I first solved in Python3 for me to understand better
# Then I solved it in Typescript after I understood the problem

# Diameter of a Binary Tree = Longest Path Between any Two Nodes


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        # Save the Longest Path Found
        self.max_diameter = 0  

       # Setting the Base Case: No Depth
        def depth(node):
            if not node:
                return 0  

            # Getting the depth of both left and right sides
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # Update max diameter at this node
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)

            # Return the height of this node
            return 1 + max(left_depth, right_depth)

        depth(root)
        return self.max_diameter


root1 = TreeNode(1)
root1.left = TreeNode(2, TreeNode(4), TreeNode(5))
root1.right = TreeNode(3)

solution_1 = Solution()
print(solution_1.diameterOfBinaryTree(root1))



print()



root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = None

solution_2 = Solution()
print(solution_2.diameterOfBinaryTree(root2))


# Link to my LeetCode Solution
# https://leetcode.com/problems/diameter-of-binary-tree/submissions/1693464581
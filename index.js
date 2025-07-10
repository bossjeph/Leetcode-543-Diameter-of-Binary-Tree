"use strict";
//  I first solved in Python3 for me to understand better
//  Then I solved it in Typescript after I understood the problem
// Diameter of a Binary Tree = Longest Path Between any Two Nodes
// Definition for a binary tree node.
class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
function diameterOfBinaryTree(root) {
    // Save the Longest Path Found
    let max_diameter = 0;
    // Setting the Base Case: No Depth
    const depth = (node) => {
        if (!node) {
            return 0;
        }
        // Getting the depth of both left and right sides
        const left_depth = depth(node.left);
        const right_depth = depth(node.right);
        // Update max diameter at this node
        max_diameter = Math.max(max_diameter, left_depth + right_depth);
        // Return the height of this node
        return 1 + Math.max(left_depth, right_depth);
    };
    depth(root);
    return max_diameter;
}
const root1 = new TreeNode(1);
root1.left = new TreeNode(2, new TreeNode(4), new TreeNode(5));
root1.right = new TreeNode(3);
console.log(diameterOfBinaryTree(root1));
console.log();
const root2 = new TreeNode(1);
root2.left = new TreeNode(2);
root2.right = null;
console.log(diameterOfBinaryTree(root2));
// Link to my LeetCode Solution
// https://leetcode.com/problems/diameter-of-binary-tree/submissions/1693497343

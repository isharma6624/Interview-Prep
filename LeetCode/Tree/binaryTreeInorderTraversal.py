class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        stack = []
        result = []
        
        curr = root
        while stack or curr:
            while curr != None:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right


        return result 
            

#iterative and recursive implementation of DFS binary tree pre-order traversal

def preOrderIterative(self,root):
    stack = []
    result = []

    curr = root
    while curr or stack:
        while curr != None:
            result.append(curr.val)
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        curr = curr.right

    return res




def preorderTraversalRec(self, root: TreeNode) -> List[int]:
        res = []
        
        if root:
            res.append(root.val)
            res = res + self.preorderTraversalRec(root.left)
            res = res + self.preorderTraversalRec(root.right)

        return res    



# insert,search, minValueNode,maxValueNode, traversal, delete in BST:
# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        elif root.val == val:
            return root
        elif root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root


    def minValueNode(self,root):
        if root.left is None:
            return root
        root.left = self.minValueNode(root.left)

    def maxValueNode(self,root):
        if root.right is None:
            return root
        root.right = self.maxValueNode(root.right)


    def searchBST(self, root, val):
           
        if root is None:
            return None
        else:
            if root.val == val:
                return root
            elif root.val > val:
                root =  self.searchBST(root.left,val)
            else:
                root = self.searchBST(root.right,val)
            
        return root

    def deleteNode(self, root, key):
        if root is None:
            return root
        
        elif root.val == key:
            
            if not root.left and not root.right: return None   #no children
            if not root.left and root.right: return root.right #1 children
            if root.left and not root.right: return root.left  #1 children
            
            #if 2 children
            pntr = root.right
            while(pntr.left):
                pntr = pntr.left
            root.val = pntr.val
            root.right = self.deleteNode(root.right,root.val)
            
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        else:
            root.right = self.deleteNode(root.right,key)
        
        return root


    def inorderTraversal(self, root):
      
        ans = []
        if root:
            ans = self.inorderTraversal(root.left)
            ans.append(root.val)
            ans = ans + self.inorderTraversal(root.right)
        return ans


    def preorderTraversal(self, root):
        ans = []
        if root:
            ans.append(root.val)
            ans = ans + self.preorderTraversal(root.left)
            ans = ans + self.preorderTraversal(root.right)

        return ans

    def postorderTraversal(self, root):
        ans = []
        if root:
            ans = self.postorderTraversal(root.left)
            ans = ans + self.postorderTraversal(root.right)
            ans.append(root.val)

        return ans

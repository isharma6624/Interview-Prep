#iterative BFS for binary tree level order traversal

from collections import deque
def BFS(self,root):

    queue = deque([root])
    res = []

    while queue:
        root = queue.popleft()
        res.append(root)
        if root.left:
            queue.append(root.left)

        if root.right:
            queue.append(root.right)


    return res 




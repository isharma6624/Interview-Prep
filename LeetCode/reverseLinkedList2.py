# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head == None:
            return None
        
        prev = None
        currentNode = head
        
        while(m > 1):
            prev = currentNode
            currentNode = currentNode.next
            m -= 1
            n -= 1
        
        connection = prev
        tail = currentNode
        
        while(n > 0):
            temp = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = temp
            n -=1 
            
        
        if connection != None:
            connection.next = prev
        else:
            head = prev
        
        tail.next = currentNode
        
        return head

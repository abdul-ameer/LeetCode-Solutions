# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node1 = headA
        node2 = headB
        
        while node1 != node2:
            node1 = headB if node1== None else node1.next
            node2 = headA if node2== None else node2.next

        
        return node1
        
        
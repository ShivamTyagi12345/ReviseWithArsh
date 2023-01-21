# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake = ListNode(0, head)
        
        seen = {0: fake}        
        prev = 0
        
        while head:
            prev += head.val            
            seen[prev] = head
            
            head = head.next
            
        head = fake
        prev = 0
        
        while head:
            prev += head.val
            head.next = seen[prev].next
            
            head = head.next
            
        return fake.next
        
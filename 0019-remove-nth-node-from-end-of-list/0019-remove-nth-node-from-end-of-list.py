# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        fast = dummy
        
        while n:
            fast = fast.next
            n-=1
        slow = dummy
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        temp = slow.next.next
        slow.next.next = None
        slow.next = temp
        
        return dummy.next
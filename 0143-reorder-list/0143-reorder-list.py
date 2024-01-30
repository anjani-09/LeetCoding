# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find the middle node
        
        fast = slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        current = slow.next
        slow.next = None
        
        #reverse the second half
        
        prev = None
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        second = prev
        first = head
        while first and second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        if second:
            first.next = second
        return head
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        p2 = self.reverse(slow.next)
        slow.next = None
        p1 = head
        
        while p2:
            temp1 = p1.next
            temp2 = p2.next
            
            p1.next = p2
            p2.next = temp1
            
            p1 = temp1
            p2 = temp2

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
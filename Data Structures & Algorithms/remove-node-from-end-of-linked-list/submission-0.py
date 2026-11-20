# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        if head is None:
            return None

        nth_node = deque(maxlen = n + 1)
        while curr != None:
            count += 1
            nth_node.append(curr)
            curr = curr.next
        if count <= n:
            return head.next
        skip = nth_node.popleft()
        skip.next = skip.next.next
        return head
        

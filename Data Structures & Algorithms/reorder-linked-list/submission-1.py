# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        a = []
        curr = head
        while curr != None:
            a.append(curr)
            curr = curr.next

        s = 0
        e = len(a)-1        
        
        while s < e:
            a[s].next = a[e]
            s += 1
            if s >= e:
                break
            a[e].next = a[s]
            e -=1
        a[s].next = None
        
        
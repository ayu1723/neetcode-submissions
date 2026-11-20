# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        curr = ListNode(0)
        temp1 = list1
        temp2 = list2
        if list1.val > list2.val:
            curr =  list2
            temp2 = temp2.next
        else:
            curr = list1
            temp1 = temp1.next
        
        temp = curr
        while temp1 != None and temp2 != None:
            if temp1.val < temp2.val: 
                temp.next = temp1
                temp1 = temp1.next
                
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        if temp1 != None :
            temp.next = temp1
        if temp2 != None :
            temp.next = temp2
        return curr
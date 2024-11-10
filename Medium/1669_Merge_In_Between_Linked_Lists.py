# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ptr1 = list1
        ptr2 = list1
        i, j = 0, 0

        while i !=a -1:
            ptr1 = ptr1.next
            i += 1 
			
        while j != b + 1:
            ptr2 = ptr2.next
            j += 1
			
        ptr1.next = list2
		
        while list2.next != None:
            list2 = list2.next
		
        list2.next = ptr2
		
        return list1
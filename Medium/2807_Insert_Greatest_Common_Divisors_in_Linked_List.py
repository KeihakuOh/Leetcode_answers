# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_gcd(self,v1,v2):
        if (v2 == 0):
            return v1
        return gcd(v2, v1%v2)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            gcd_val = self.get_gcd(curr.val, curr.next.val)
            node = ListNode(gcd_val, curr.next)
            curr.next = node
            curr = curr.next.next

        return head


    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        val = []
        ans = 0
        while(head):
            val.append(head.val)
            head = head.next
        num = len(val)
        for i in range(int(num/2)):
            ans = max(ans, val[i] + val[num - 1 -i])
        return ans
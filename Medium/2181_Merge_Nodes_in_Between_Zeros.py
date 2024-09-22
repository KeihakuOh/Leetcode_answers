# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        start = False
        sum = 0
        while curr:
            if curr.val == 0 and start == False:
                answer = ListNode(sum)
                answer_curr = answer
                sum = 0
                curr = curr.next
                start = True
            elif curr.val == 0 and start == True:
                node = ListNode(sum)
                answer_curr.next = node
                answer_curr = node
                sum = 0
                curr = curr.next
            else:
                sum += curr.val
                curr = curr.next
        return answer
        

# maybe better answer
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         l = head
#         r = head.next

#         sum = 0
#         while r:
#             if r.val == 0:
#                 l = l.next
#                 l.val = sum
#                 sum = 0
#             else:
#                 sum += r.val
#             r = r.next
        
#         l.next = None
#         return head.next
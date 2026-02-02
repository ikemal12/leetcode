# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counts = {}
        while head:
            num = head.val
            counts[num] = 1 + counts.get(num, 0)
            head = head.next
        
        dummy = cur = ListNode()
        for num, count in counts.items():
            cur.next = ListNode(count)
            cur = cur.next
        return dummy.next

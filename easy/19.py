#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for _ in range(n + 1): fast = fast.next  # fast đi trước n+1 bước
        while(fast != None):                      # đi đồng thời đến khi fast = None
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next                # bypass node cần xóa
        return dummy.next
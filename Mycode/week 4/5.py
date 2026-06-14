#https://leetcode.com/problems/merge-k-sorted-lists/
#23. Merge K Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node: heapq.heappush(heap, (node.val, i, node))  # (val, index, node) để tránh so sánh ListNode

        dummy = ListNode(0)
        cur = dummy
        while(heap):
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next: heapq.heappush(heap, (node.next.val, i, node.next))  # push node tiếp theo của list đó

        return dummy.next
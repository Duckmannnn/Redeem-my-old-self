#https://leetcode.com/problems/linked-list-cycle/
#141. Linked List Cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vis = {}
        while(head != None):
            if head in vis: return True
            vis[head] = True
            head = head.next
        return False
    
# Floyd's cycle detection
# slow, fast = head, head
# while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next
#     if slow == fast: return True
# return False

#that inplementation is very clean and less space
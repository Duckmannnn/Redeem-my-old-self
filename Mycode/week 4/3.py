#https://leetcode.com/problems/design-linked-list/
#707. Design Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.dummy = Node(0)  # sentinel head, tránh edge case
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: return -1
        cur = self.dummy.next
        for _ in range(index): cur = cur.next  # đi đến đúng node
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: return
        cur = self.dummy
        for _ in range(index): cur = cur.next  # dừng ở node TRƯỚC index
        node = Node(val)
        node.next, cur.next = cur.next, node   # insert
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: return
        cur = self.dummy
        for _ in range(index): cur = cur.next  # dừng ở node TRƯỚC index
        cur.next = cur.next.next               # bypass
        self.size -= 1
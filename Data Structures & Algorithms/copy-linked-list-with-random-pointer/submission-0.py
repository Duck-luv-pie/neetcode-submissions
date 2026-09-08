"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 1. Insert copied nodes after each original node
        cur = head

        while cur:
            copy = Node(cur.val)
            copy.next = cur.next
            cur.next = copy
            cur = copy.next

        # 2. Assign random pointers for copied nodes
        cur = head

        while cur:
            copy = cur.next

            if cur.random:
                copy.random = cur.random.next

            cur = copy.next

        # 3. Separate the original list and copied list
        cur = head
        copy_head = head.next

        while cur:
            copy = cur.next
            cur.next = copy.next

            if copy.next:
                copy.next = copy.next.next

            cur = cur.next

        return copy_head
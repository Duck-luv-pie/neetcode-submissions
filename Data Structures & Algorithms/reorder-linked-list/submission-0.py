# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #first we want to find the middle of the linked list

        mid, end = head, head

        while end and end.next:
            mid = mid.next
            end = end.next.next

        #now mid is at the end, so we can do in place reversal to get the right ordering we need

        prev = None
        cur = mid

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        #now we have reversed the list we need to put it in a new list
        first = head
        second = prev

        while second.next:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2



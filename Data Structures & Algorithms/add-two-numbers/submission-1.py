# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #we can put it in a dummyNode
        dummy = tail = ListNode()
        carry = False

        #go through it if both lists exist or if there is a carry that exists
        #sum it all up and modullus for what the value is and check if we have carry over
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            if carry:
                summation = l1_val + l2_val + 1
            else:
                summation = l1_val + l2_val
            
            value = summation % 10

            if value != summation:
                carry = True
            else:
                carry = False
            
            tail.next = ListNode(value)
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
    
        return dummy.next



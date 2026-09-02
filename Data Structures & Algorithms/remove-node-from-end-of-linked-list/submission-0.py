# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #we gotta have two pointers which are n apart.
        
        dummy = ListNode(0, head) #0, head
        res = dummy
        delete = head
        trailblazer = head
        for i in range(n - 1):
            trailblazer = trailblazer.next


        while trailblazer.next:
            trailblazer = trailblazer.next
            dummy = dummy.next
            delete = delete.next
        
        #now we have the one we need to delete
        dummy.next = delete.next

        return res.next #(our head)
        #if you create a dummy you almost always return dummy.next
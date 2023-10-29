class ListNode:
    def __init__ (self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseLinkedList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head     #two pointers   
        while curr:
            nxt = curr.next  #save the next node to iterate
            curr.next = prev
            prev = curr
            curr = nxt

        return prev     # return prev because the curr is Null
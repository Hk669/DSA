class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head, k):
        """
        :type head:ListNode
        :type k: int
        :rtype : ListNdoe
        """
        dummy = ListNode(0)
        dummy.next = head
        ptr1 = dummy
        ptr2 = dummy

        for _ in range(k):
            ptr2 = ptr2.next

        node1 = ptr2

        while ptr2 is not None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        node2 = ptr1

        temp = node1.val
        node1.val = node2.val
        node2.val = temp

        return dummy.next
    
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def cycleList(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            
            slow = slow.next
            fast = fast.next.next

        return True
    

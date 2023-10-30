class ListNode:
    def __init__ (self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddleNode(self, head):

        if not head or not head.next:
            return None
        
        dummy = ListNode()
        tail = dummy # keep a track of list
        slow_ptr = head # to point the middle node
        fast_ptr = head # to achive the middle element

        while fast_ptr and fast_ptr.next:
            tail.next = slow_ptr
            tail = tail.next
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        tail.next = slow_ptr.next

        return dummy.next
    
# refer helperimgs/2095.png
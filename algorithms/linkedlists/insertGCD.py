class ListNode:
    def __init__ (self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a%b
        return a
    
    def insertGCDs(self,head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        
        curr = head

        while curr and curr.next:
            gcd = self.gcd(curr.val, curr.next.val)

            new_node = ListNode(gcd)
            new_node.next = curr.next
            curr.next = new_node

            curr = curr.next.next

        return head
    
# refer hrlperimgs/GCDinsert.png
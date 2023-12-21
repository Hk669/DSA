class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self):
        new_node = ListNode(0)
        if self.head is None:
            self.head = new_node
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.val)
            curr = curr.next
        return elements
    
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        ptr1 = dummy
        ptr2 = dummy

        for _ in range(n+1):
            ptr2 = ptr2.next

        while ptr2 is not None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        ptr1.next = ptr1.next.next

        return dummy.next



# prep
class ListNode:
    def __init__(self,head):
        self.head = head
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self):
        node = ListNode(0)
        if self.head is None:
            self.head = node
        
        curr = self.head
        while curr:
            curr = curr.next
        curr.next = node
        
class Sol:
    def removeNthNode(self,head, n):

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(n+1):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next

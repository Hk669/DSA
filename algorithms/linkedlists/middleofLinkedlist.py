class ListNode:
    def __init__ (self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self):
        new_node = ListNode(self.val)
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
    def middleNode(self, head):
        if not head:
            return None
        
        slow_ptr = head
        fast_ptr = head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr
    
# refer helperimgs/876.png

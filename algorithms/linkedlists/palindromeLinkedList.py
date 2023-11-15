class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self):
        new_node = ListNode(val)
        if self.head == None:
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
    def palindromeLinkedList(self, head):
        """
        :type head : ListNode
        :rtype : bool
        """
        if not head or not head.next:
            return True
        list = []
        while head:
            list.append(head.val)
            head = head.next
        
        if list == list[::-1]:
            return True
        else:
            return False

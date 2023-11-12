class ListNode:
    def __init__ (self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.val)
            current = current.next
        return elements
    

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
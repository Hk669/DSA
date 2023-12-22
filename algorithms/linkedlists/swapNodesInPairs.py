class ListNode:
    def __init__(self, val=0, next = None):
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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype : ListNode
        """

        if head:
            dummy = ListNode(0)
            dummy.next = head
            curr = dummy

            while curr.next and curr.next.next:

                node1 = curr.next
                node2 = curr.next.next

                curr.next = node2 #updates the 3rd node
                node1.next = node2.next
                node2.next = node1

                curr = node1 #updates to the 2nd node

            return dummy.next
        return head

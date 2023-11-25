class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self):
        new_node = ListNode(self.val)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

        self.head = new_node

    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.val)
            curr = curr.next
        return elements
    
class Solution:
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """

        elements = []
        curr = head
        while curr:
            elements.append(curr.val)
            curr = curr.next

        binNum = ''.join(map(str,elements))
        res = int(binNum,2)

        return res
    

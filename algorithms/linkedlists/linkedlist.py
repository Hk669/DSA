# practice

class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
        
    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next_node

    
linkedlist = LinkedList()
linkedlist.append(5)
linkedlist.append(7)
linkedlist.append(9)

linkedlist.traverse()
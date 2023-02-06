import os
os.system('cls')

#Dynamic Allocation Example
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

linkedList = linkedList()
linkedList.add_node(1)
linkedList.add_node(2)
linkedList.add_node(3)

print(linkedList.head.data)
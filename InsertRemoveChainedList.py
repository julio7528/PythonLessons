import os 
os.system('cls')
#Inserting in Chained List
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return 
        last = self.head 
        while(last.next):  #while last node points to another node 
            last = last.next #jump to next node 
        last.next = new_node #make last node point to new node 

    def print_list(self):
        temp = self.head 
        while(temp): #while temp points to a node 
            print(temp.data) #print data in that node
            temp=temp.next #jump to next node 
        print()   #print an empty line after printing list  

    def remove_node(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None

        
linkedList = linkedList()

linkedList.insert_at_beginning(1)
linkedList.insert_at_beginning(2)
linkedList.insert_at_beginning(3)
linkedList.insert_at_beginning(4)
linkedList.insert_at_beginning(5)
linkedList.insert_at_end(6)
linkedList.insert_at_end(7)
linkedList.insert_at_end(8)
linkedList.insert_at_end(9)

#Discover the length of the Chained List
temp = linkedList.head
length = 0
while(temp):
    length += 1
    temp = temp.next
print("Length of the list is", length)
linkedList.remove_node(length)

#Discover the start value of the Chained List   
temp = linkedList.head
start = temp.data   
print("Start value of the list is", start)
linkedList.remove_node(start)

print("The list with items removed is:") 
linkedList.print_list()


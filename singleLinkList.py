class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Single:
    def __init__(self):
        self.head = None
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        align  = self.head

        while align.next != None:
            align = align.next
        align.next = new_node

    def display(self):
        pointer = self.head
        while pointer != None:
            print(pointer.data, end="==>")
            pointer = pointer.next
        print("None")


    def delete(self,key):
        pre = None
        temp = self.head

        if temp != None and temp.data == key:
            self.head = temp.next
            temp = None
            return
        
        while temp != None and temp.data != key:
            pre = temp
            temp = temp.next

        if temp == None:
            print("value not found")
            return
        pre.next = temp.next
        temp = None

        print("value deleted", key)
            

s = Single()
s.insert_end(10)
s.insert_end(20)
s.insert_front(5)
s.insert_front(63)
s.display()
s.delete(20)
s.display()
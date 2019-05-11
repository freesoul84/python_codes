class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
           self.head = new_node
           return
        last = self.head
        while (last.next):
            last = last.next

        last.next =  new_node

    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next

if __name__=="__main__":
    l=LinkedList()
    l.append(3)
    l.append(4)
    l.append(5)
    l.display()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def getCount(self):
        count = 0
        temp = self.head
        while (temp is not None):
            count+=1
            temp = temp.next
        return count

    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next

if __name__=="__main__":
    llist = LinkedList()
    llist.head  = Node(1)
    second = Node(2)
    third  = Node(3)
    llist.head.next=second
    second.next=third
    print(llist.getCount())
    llist.display()

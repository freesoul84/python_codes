class Node:
    def __init__(self,data):
        self.head=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def check(self):
        temp=self.head
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        if count%2==1:
            return "Odd"
        else:
            return "Even"

if __name__=="__main__":
    li=LinkedList()
    li.head=Node(1)
    second=Node(2)
    third=Node(3)
    fourth=Node(4)
    li.head.next=second
    second.next=third
    third.next=fourth
    print(li.check())

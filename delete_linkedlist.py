import math
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next

    def count(self):
        count=0
        temp=self.head
        while temp is not None:
            count+=1
            temp=temp.next

        return count

    def delete_middle(self):
        c=self.count()
        print("count",c)
        count1=1
        temp=self.head
        while temp is not None:
            if math.ceil(c/2)-1==count1:
                print("tempdata",temp.data)
                temp.next=temp.next.next
                break
            temp=temp.next
            count1+=1

if __name__=="__main__":
    l=LinkedList()
    l.head=Node(1)
    s=Node(2)
    t=Node(3)
    f=Node(4)
    fi=Node(5)
    l.head.next=s
    s.next=t
    t.next=f
    f.next=fi
    l.display()
    l.delete_middle()
    l.display()

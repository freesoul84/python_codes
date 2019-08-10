class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def getCount(self):
        temp=self.head
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        print("count",count)
        if count%2==0:
            return (count//2)+1
        elif count%2==1:
            return (count//2)+1

    def getMiddle(self,co):
        temp=self.head
        c=1
        while temp.next is not None:
            if c==co:
                return temp.data
            temp=temp.next
            c+=1
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
    count=l.getCount()
    print(count)
    print(l.getMiddle(count))

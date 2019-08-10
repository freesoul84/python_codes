class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
        print("\n")

def linkedmerging(head1,head2,head3):
    temp1=head1
    temp2=head2
    temp3=head3
    if temp1.data<temp2.data:
        temp3.head=Node(temp1.data)
        temp1=temp1.next
    elif temp1.data>temp2.data:
        temp3.head=Node(temp2.data)
        temp2=temp2.next
    temp3=temp3.head
    while temp1!=None and temp2!=None:
        if temp1.data<temp2.data:
            temp3.next=Node(temp1.data)
            temp1=temp1.next
        elif temp1.data>temp2.data:
            temp3.next=Node(temp2.data)
            temp2=temp2.next
        temp3=temp3.next
        if temp1==None:
            temp3.next=Node(temp2.data)
        if temp2==None:
            temp3.next=Node(temp3.data)
    head3.display()
if __name__=="__main__":
    link1=LinkedList()
    link2=LinkedList()
    link3=LinkedList()
    link1.head=Node(11)
    link2.head=Node(21)
    a1=Node(35)
    b1=Node(58)
    c1=Node(79)
    a2=Node(41)
    b2=Node(61)
    c2=Node(811)
    link1.head.next=a1
    link2.head.next=a2
    a1.next=b1
    b1.next=c1
    a2.next=b2
    b2.next=c2
    link1.display()
    link2.display()
    linkedmerging(link1.head,link2.head,link3)

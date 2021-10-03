class Node:
    def __init__(self,Value):
        self.value= Value
        self.Next= None

class Linked_list:
    def __init__(self):
        self.head=None
    def items(self):
        sum =0
        current = self.head
        while current:
            sum +=1
            current=current.Next
        return sum

    def insertatbegin(self,Data):
        if self.head == None:
            print ('empty!')
        else:
            newnode=Node(Data)
            
            newnode.Next= self.head
            self.head= newnode

    def insertinthemiddle(self,anode,data):
        newnode = Node(data)
        newnode.Next= anode.Next
        anode.Next=newnode

    def insertatend(self,Data):
        newnode=Node(Data)
        last=self.head()
        while(last.Next):
            last =last.Next
        last.Next = newnode

    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.value)
            temp=temp.Next



s= Linked_list()
node1=Node(5)
node2=Node(7)
node3=Node(8)
node4=Node(10)

node1.Next=node2
node2.Next=node3
node3.Next=node4
s.head=node1

s.insertinthemiddle(s.head.Next, 10)

s.printlist()
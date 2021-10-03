class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def addllelements(head):
    current = head
    sum=current.data
    while current.next != None:
        sum=current.next.data+sum
        current=current.next
    return sum

def printelements(head):
    current = head
    print(current.data)
    while current.next != None:
        print(current.next.data)
        current=current.next


node1=Node (5)
node2=Node (6)
node3=Node (21)
node4=Node (5684)
node5=Node (545)


node1.next =node2
node2.next=node3
node3.next=node4
node4.next=node5


head = node1


printelements(node1)
print(addllelements(node1))
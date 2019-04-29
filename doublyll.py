#Doubly Linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def insert(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            currentnode=self.head
            while currentnode.next is not None:
                currentnode=currentnode.next
            currentnode.next=newNode
            newNode.prev=currentnode

    def printlist(self):
        currentnode=self.head
        while currentnode is not None:
            print(currentnode.data)
            currentnode=currentnode.next        

firstnode=Node("Ghanshyam")
sencodnode=Node("Naresh")
thirdnode=Node("Chetan")
linkedlist=Linkedlist()
linkedlist.insert(firstnode)
linkedlist.insert(sencodnode)
linkedlist.insert(thirdnode)
linkedlist.printlist()

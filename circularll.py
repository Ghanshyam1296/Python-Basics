#Circular linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def insert(self,newNode):
        if self.head is None:
            self.head=newNode
            newNode.next=self.head
        else:
            currentnode=self.head
            while currentnode.next is not self.head:
                currentnode=currentnode.next
            currentnode.next=newNode
            newNode.next=self.head

    def printlist(self):
        currentnode=self.head
        while True:
            print(currentnode.data)
            if currentnode.next==self.head:
                break
            currentnode=currentnode.next

    def insertbig(self,newNode):
        if self.head is None:
            self.head=newNode
            newNode.next=self.head
        else:
            temp=self.head
            self.head=newNode
            newNode.next=temp

firstnode=Node("Ghanshyam")
sencodnode=Node("Naresh")
thirdnode=Node("Chetan")
zeronode=Node("Hastimal")
linkedlist=Linkedlist()
linkedlist.insert(firstnode)
linkedlist.insert(sencodnode)
linkedlist.insert(thirdnode)
linkedlist.insertbig(zeronode)
linkedlist.printlist()
            
        

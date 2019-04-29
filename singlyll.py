#singally linked list

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def insert(self,newNode):

        if self.head is None:
            self.head=newNode
        else:
            lastnode=self.head
            while lastnode.next is not None:
                lastnode=lastnode.next
            lastnode.next=newNode

    def printlist(self):
        currentnode=self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data,end='->')
            currentnode=currentnode.next

    def insertbig(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            temp=self.head
            self.head=newNode
            newNode.next=temp
    
        


firstnode=node("Ghanshyam")
sencodnode=node("Naresh")
thirdnode=node("Chetan")
zeronode=node("Hastimal")
fifthnode=node("Ghanshyam")
linkedlist=Linkedlist()
linkedlist.insert(firstnode)
linkedlist.insert(sencodnode)
linkedlist.insert(thirdnode)
linkedlist.insertbig(zeronode)
linkedlist.insert(fifthnode)
linkedlist.printlist()

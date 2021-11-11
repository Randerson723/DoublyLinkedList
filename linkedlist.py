class Node:
    def __init__(self, dataval, nextnode = None, prevnode = 0):
        self.dataval = dataval
        self.prevnode = None
        self.nextnode = nextnode


class doublylinkedist:
    def __init__(self, new_node = 0):
        self.startnode = None
        self.nextnode = None
        self.new_node = new_node

    #Inserting into an empty list
    def InserttoEmptyList(self, data, new_node = 0):
        if self.startnode is None:
            self.new_node = data
            self.nextnode = new_node
        else:
            print("List is Empty")


    def InsertatEnd(self, data, new_node = 0):
        if self.startnode is None:
            self.new_node = data
            self.startnode = new_node
            return
        n = self.startnode
        #Iterate till the next reaches NULL
        while new_node is not None:
            node = self.nextnode
            new_node = data
            self.nextnode = new_node
            self.prevnode = node

    # Delete Items from the start
    def DeleteStart(self):
        if self.startnode is None:
            print("List is Empty, no element to delete")
            return
        if self.startnode.next is None:
            self.startnode = None
            return
        self.startnode = self.startnode.next
        self.prevnode = None

    #Delete Items from the End
    def DeleteEnd(self):
        if self.startnode is None:
            print("List is Empty, no element to delete")
            return
        if self.startnode is None:
            self.startnode = None
            return
        n = self.startnode
        while self.startnode is not None:
            n = self.nextnode
        self.startnode = None


    #Displaying each element
    def Display(self, startnode = 0):
        if self.startnode is None:
            print("List is Empty")
            return
        else:
            n = self.startnode
            while n is not None:
                print("Element is:", n.item)
                n = self.nextnode
        print("\n")


n1 = Node(dataval=10)
n2 = Node(dataval=40)
n3 = Node(dataval= 60)




NewDoublyLinkedList = doublylinkedist()






NewDoublyLinkedList.InsertatEnd(40)
import time

begin = time.time()
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insAtBeg(self,new_data):
        newNode = node(new_data)
        newNode.next = self.head
        self.head = newNode

    def insAfter(self,prevNode,new_data):
        if prevNode is None:
            print("Invalid!!")
            return
        newNode = node(new_data)
        newNode.next = prevNode.next
        prevNode.next = newNode

    def insAtEnd(self, new_data):
        newNode = node(new_data)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = newNode

    def search(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False
    
    def lastelement(self):
        last = self.head 
        while last.next:
            last = last.next
        print("The last word in the linked list is ",last.data)

    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next


llist = LinkedList()
llist.insAtEnd("Apple")
llist.insAtBeg("Mosambi")
llist.insAtBeg("Orange")
llist.insAtEnd("Tomato")
llist.insAfter(llist.head.next, "Mango")
print('linked list:')
llist.printList()


print()
item_to_find = "Orange"
if llist.search(item_to_find):
    print(str(item_to_find) + " is found")
else:
    print(str(item_to_find) + " is not found")


item_to_find = "banana"
if llist.search(item_to_find):
    print(str(item_to_find) + " is found")
else:
    print(str(item_to_find) + " is not found")


print("The first word in the linked list is",llist.head.data)
llist.lastelement()
end = time.time()
print(f"Total runtime of the program is {end - begin}")
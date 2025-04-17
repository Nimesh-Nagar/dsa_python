# Singly Linked list 

class Node:
    def __init__(self, data=None, next= None):
        self.data = data
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None

    # This function prints the contents of
    # the linked list starting from the head

    def printList(self):
        if self.head == None:
            print("Linked-List is empty")
            return
        
        current = self.head
        while current:
            print(current.data, end=" ---> ")
            current = current.next
        print("NULL")

    # Length of linked list 
    def length_ll(self):
        if self.head is None:
            return 0
        
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next

        return counter

    # Insert node at Beginning 
    def insert_at_beginning(self, value):
        node = Node(value, self.head)
        self.head = node

    # insert node at End
    def insert_at_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node    

    # insert at any index 
    def insert_at_index(self, index, value):
        if index < 0 and index > self.length_ll():
            raise Exception 
        
        if index == 0:
            self.insert_at_beginning(value)

        counter = 0 
        current = self.head
        while current:
            if counter == index - 1:
                new_node = Node(value, current.next)
                current.next = new_node
                break

            current = current.next
            counter += 1
        



ll = LinkedList()

# ll.insert_at_beginning(44)
# ll.insert_at_beginning(22)
# ll.insert_at_beginning("Nimesh")

# ll.printList()
# print(ll.length_ll())

ll.insert_at_end(67)
ll.insert_at_end(65)
ll.insert_at_end(45)

ll.printList()
print(ll.length_ll())

ll.insert_at_index(1, 30)    
ll.printList()


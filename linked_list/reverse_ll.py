# reverse linked list

class Node:
    def __init__(self, data=None, next= None):
        self.data = data
        self.next = next 

def reverse_linkList(head):

    # Initialize three pointers: curr, prev and next
    current = head
    prev = None

    # Traverse all the nodes of Linked List
    while current is not None:

        # store next
        nxtNode = current.next

        # Reverse current node's next pointer
        current.next = prev

        # Move pointers one position ahead
        prev = current
        current = nxtNode 

    # Return the head of reversed linked list
    return prev


def printList(node):
    while node is not None:
        print(f" {node.data}", end="")
        node = node.next
    print()

if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Given Linked list:", end="")
    printList(head)

    head = reverse_linkList(head)

    print("Reversed Linked List:", end="")
    printList(head)



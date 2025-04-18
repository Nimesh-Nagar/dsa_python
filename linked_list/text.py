#User function Template for python3
'''
    Your task is to insert a new node in 
	the middle of the linked list with
	the given value.
	
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
	
	Function Arguments: head (head of linked list), node 
	(node to be inserted in middle)
	Return Type: None, just insert the new node at mid.
'''
#Function to insert a node in the middle of the linked list.
class Solution:
    def get_len(self,head):
        count = 0
        temp = head
        
        while temp:
            count += 1
            temp = temp.next
        return count
        
    
    def insertInMiddle(self, head, x):
        #code here
        
        ll_length = self.get_len(head)
        
        mid = ll_length//2
        counter = 0
        
        if mid == 0:
            head = Node(x)
        
        current = head
        counter = 0
        while current:
            if counter == mid - 1:
                new_node = Node(x, current.next)
                current.next = new_node
                break
            
            current = current.next
            counter += 1 
          


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0].strip())
    idx = 1

    while t > 0:
        arr = list(map(int, data[idx].strip().split()))
        x = int(data[idx + 1].strip())
        idx += 2

        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for num in arr[1:]:
                tail.next = Node(num)
                tail = tail.next

        ob = Solution()
        ans = ob.insertInMiddle(head, x)
        printList(ans)
        print("~")
        t -= 1
# } Driver Code Ends
# Implementation of Queue using Array
'''
Ref Article : https://www.geeksforgeeks.org/array-implementation-of-queue-simple/

A simple array implementation discussed here is not used in practice as it is not efficient. In practice, we either use Linked List Implementation of Queue or circular array implementation of queue.
'''



class Queue:
    def __init__(self):
        self.q = []

    def is_empty(self):
        return len(self.q) == 0

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if not self.is_empty():
            self.q.pop(0)

    def get_front(self):
        return -1 if self.is_empty() else self.q[0]

    def display(self):
        print(' '.join(map(str, self.q)))

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.get_front())
    q.dequeue()
    q.enqueue(4)
    q.display()


"""
Time Complexity: 
O(1) for Enqueue (element insertion in the queue) as we simply increment pointer and put value in array, 
O(n) for Dequeue (element removing from the queue).

Auxiliary Space: 
O(n), as here we are using an n size array for implementing Queue

We can notice that the Dequeue operation is O(n) which is not acceptable. 
The enqueue and dequeue both operations should have O(1) time complexity. 
That is why if we wish to implement a queue using array (because of array advantages like cache friendliness and random access), we use 'circular array implementation of queue'. 
"""
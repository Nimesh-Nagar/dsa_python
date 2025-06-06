'''  155. Min Stack [LeetCode]
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]

        
# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.push(-1)
obj.push(4)
obj.push(-3)
print("Stack       : ",obj.stack)
print("TOP ELEMENT : ",obj.top())
print("Min Element : ",obj.getMin())

obj.pop()
print("Stack       : ",obj.stack)
print("TOP ELEMENT : ",obj.top())
print("Min Element : ",obj.getMin())
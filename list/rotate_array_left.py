# Rotate array left(Counter Clockwise) Direction by D step 

arr = [10,20,30,40,50]
print(f"Original Array :\t {arr}")

step = 2
size = len(arr)
step =  step % size  # Adjust D to handle cases where D is greater than array length

# METHOD 1        
# arr[:] = arr[step:] + arr[:step]

arr[:] = reversed(arr)  # Reverse the entire array
arr[:size-step] = reversed(arr[:size-step])  # Reverse the first N-D elements
arr[size-step:] = reversed(arr[size-step:])  # Reverse the remaining elements
print(f"After Left Rotating {step} times : {arr}")

# METHOD 2

temp = arr[:step]
for idx in range(step,len(arr)):
    arr[idx-step] = arr[idx]

for idx in range(0,len(temp)):
    arr[size-step+idx] = temp[idx] 

print(f"After Left Rotating {step} times : {arr}")

# Method 3 

def reverse(arr, start, stop):
    while start < stop:
        arr[start], arr[stop] = arr[stop], arr[start]
        start += 1
        stop -= 1

step = step % size

reverse(arr, 0, step-1)     # Reverse the first D(step) elements
reverse(arr, step, size-1)  # Reverse the remaining elements
reverse(arr, 0, size-1)     # Reverse the entire array

print(f"After Left Rotating {step} times : {arr}")








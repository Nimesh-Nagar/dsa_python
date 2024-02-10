# Rotate array Right(Clockwise) Direction by D step 

def rotate_array(arr,size,step_d):
    def reverse(l, start, end):
        while start < end:
            l[start], l[end] = l[end], l[start]
            start += 1
            end -= 1

    step_d %= size
    reverse(arr, size-step_d, size-1)   # Reverse number elements what to rotate (step_d)
    reverse(arr, 0, size-step_d-1)      # Reverse remaining elements
    reverse(arr, 0, size-1)             # Reverse entire arrar

    return arr

arr = [10,20,30,40,50,60]
print("ORIGINAL Array :\t ",arr)
size = len(arr)
step_d = 2
print(f"After Right Rotating {step_d} times : ",rotate_array(arr,size,step_d))
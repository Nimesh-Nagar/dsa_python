# find Square root of a given number using Binary search;
def floor_square(num):

    #base condition
    if num == 0 or num == 1:
        return num
    
    low = 1
    high = num//2
    ans = -1
    while low <= high:
        mid = (low + high) // 2

        if mid*mid == num:
            return mid
        
        elif mid*mid < num:
            low = mid + 1
            ans = mid

        # it terminates the while loop and returns the ans value
        else:
            high = mid - 1  

    return ans


given_num = int(input("Enter the NUmber : "))

sqr = floor_square(given_num)
print(f"Square root of {given_num} is {sqr}")

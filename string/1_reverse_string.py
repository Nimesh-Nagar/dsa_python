given_string = "nimesh nagar" 
# given_string = "abhishek sahu" 
print("------------ Method 1 : using string slicing ------------")
print(f"Original String : {given_string}")
print("Reversed String : ",given_string[::-1]) # power of pyhton 

# ------------ using for loop ------------ 
 
def reverse_str(str):
    rev_str = ""
    for ch in str:
        rev_str = ch + rev_str 

    return rev_str

print("------------ Method 2 : using for loop ------------")
str = input("Enter string to reverse : ")
print(f"Original Sting : {str}")
print("Reversed String : ",reverse_str(str))

# Time complexity == O(n)
# Auxilary Space == O(1)

# ------------ using recursion -------------

def reverse_string(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])

print(" ------------ Method 3 : Using Recursion ------------")
ans = reverse_string("hello")
print("Original String : hello")
print("Reversed String : ",ans)


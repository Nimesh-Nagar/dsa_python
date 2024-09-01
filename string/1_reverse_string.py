given_string = "nimesh nagar" 
# given_string = "abhishek sahu" 
print(given_string[::-1]) # power of pyhton 

#using for loop

def reverse_str(str):
    rev_str = ""
    for ch in str:
        rev_str = ch + rev_str 

    return rev_str

str = input("Enter string to reverse ")
print(f"Original Sting : {str}")

print(reverse_str(str))

# Time complexity == O(n)
# Auxilary Space == O(1)

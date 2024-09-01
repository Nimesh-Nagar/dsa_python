''' 
Given a string, write a python function to check if it is palindrome or not. 
A string is said to be palindrome if the reverse of the string is the same as string. 
For example, “radar” is a palindrome, but “radix” is not a palindrome.

'''

# def check_palindrome(given_str):
#     rev = given_str[::-1] 
#     if rev == given_str:
#         return True
#     else:
#         return False 

# # given_str = 'radar'
# given_str = 'radix'

# print(f"String '{given_str}' is palindrome ? {check_palindrome(given_str)}")

def isPalindrome(str):
    rev = ''
    for ch in str:
        rev = ch + rev

    return rev == str 

# str = "malayalam"
str = "geeks"

ans = isPalindrome(str)

if ans:
    print("YES")
else:
    print("NO")

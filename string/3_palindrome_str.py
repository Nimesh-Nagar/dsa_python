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

print("----- Naive Technique -----")
print(isPalindrome("malayalam"))
print(isPalindrome("geeks"))

'''
Time complexity : O(n)
space complexity : O(n) (new reversed string is crested)
'''

# -------------- (Two Pointer Technique) ----------

def is_palindrome(str):
    left = 0 
    right = len(str) - 1

    while left <= right:
        if str[left] != str[right]:
            return False
        else:
            left += 1
            right -= 1

    return True

print("---- Using Two Pointer Technique (Optimised) ------ ")
print(is_palindrome("radar"))
print(is_palindrome("geeks"))


# ------- using Recurion ------

def is_palindrome(s):
    if len(s) <= 1:  # Base case: single character or empty string
        return True
    if s[0] != s[-1]:  # Compare first and last characters
        return False
    return is_palindrome(s[1:-1])  # Recur for the remaining substring

# Example Usage:
print("---- Using Recrsion ----")
print(is_palindrome("madam"))  
print(is_palindrome("hello"))  
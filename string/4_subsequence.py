# In this problem, we are given two strings s1 and s2 of different sizes. 
# Our task is to find out that string s2 is a subsequence of string s1 or not.

# --------------------------------------------------------------
# METHOD 1 Nive solution (Two Pointer approch)
# --------------------------------------------------------------

def issubseq(s1, s2):

    if not s2:  # Edge case: Empty s2 is always a subsequence
        return True
    if not s1:  # Edge case: Non-empty s2 can't be a subsequence of empty s1
        return False

    i, j = 0, 0 # 2 pointers 
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            j += 1

        i += 1 #  # Always move s1 pointer

    if j == len(s2):
        return True
    else: 
        return False
    
s1 = "ABCDEF"
s2 = "ADE"
print("METHOD 1: Two Pointer Technique")
print(issubseq(s1,s2))             # True
print(issubseq("ABCDEF", "ADEE"))  # False
print(issubseq("", "a"))           # False (Empty s1)
print(issubseq("abc", ""))         # True (Empty s2 is always a subsequence)


"""
Time complexity : O(N)
Space Complexity : O(1) efficient
"""

# --------------------------------------------------------------
# METHOD 2 : Recursive Approch
# --------------------------------------------------------------

def isSubseq_rec(s1, s2, len_s1, len_s2):
    
    if len_s2 == 0:
        return True 
    if len_s1 == 0:
        return False 
    
    if s1[len_s1-1] == s2[len_s2-1]:
        return isSubseq_rec(s1, s2, len_s1-1, len_s2-1)
    else: 
        return isSubseq_rec(s1, s2, len_s1-1, len_s2)

s1 = "ABCDEF"
s2 = "ABF"

len_s1 = len(s1)
len_s2 = len(s2)

print("METHOD 2: Recursive")
print(isSubseq_rec(s1, s2, len_s1, len_s2)) # True
print(isSubseq_rec("ABCDEF", "ADEE", len("ABCDEF"), len("ADEE"))) # False






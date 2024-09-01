# In this problem, we are given two strings s1 and s2 of different sizes. 
# Our task is to find out that string s2 is a subsequence of string s1 or not.

# --------------------------------------------------------------
# METHOD 1 Nive solution 
# --------------------------------------------------------------

def issubseq(s1, s2):
    i, j = 0, 0 

    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            j += 1
        else:
            i += 1 
    if j == len(s2):
        return True
    else: 
        return False
    
s1 = "ABCDEF"
s2 = "ADE"
print("METHOD 1 Result")
print(issubseq(s1,s2)) # True

# --------------------------------------------------------------
# METHOD 2 : Recursive 
# --------------------------------------------------------------

def isSubseq(s1, s2, len_s1, len_s2):
    
    if len_s2 == 0:
        return True 
    if len_s1 == 0:
        return False 
    
    if s1[len_s1-1] == s2[len_s2-1]:
        return isSubseq(s1, s2, len_s1-1, len_s2-1)
    else: 
        return isSubseq(s1, s2, len_s1-1, len_s2)

s1 = "ABCDEF"
s2 = "DEA"

len_s1 = len(s1)
len_s2 = len(s2)

print("METHOD 2 Result")
print(isSubseq(s1, s2, len_s1, len_s2)) # False





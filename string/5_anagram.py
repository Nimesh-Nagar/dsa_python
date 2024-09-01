# Check whether two Strings are anagram of each other
'''
An anagram of a string is another string that contains the same characters, 
only the order of characters can be different. 
For example, “abcd” and “dabc” are an anagram of each other.
"listen" and "silent" are an anagram of each other.
"aabc" and "cabb" not an anagram
'''
# -----------------------------------------------
# METHOD 1 
# -----------------------------------------------

def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    temp1 = sorted(s1)
    temp2 = sorted(s2)
    return temp1 == temp2
    

s1 = "listen"
s2 = "silent"
print(isAnagram(s1,s2)) 

# time complexity is O(nlogn) 
# auxilary space complexity O(n) 

# -----------------------------------------------
# METHOD 2 
# -----------------------------------------------

def checkAnagram(s1,s2):
    if len(s1) != len(s2):
        return False
    
    counter = [0]*256

    for idx in range(len(s1)):
        counter[ord(s1[idx])] += 1
        counter[ord(s2[idx])] -= 1  

    for val in counter:
        if val != 0:
            return False
    return True 

# s1 = "listen"
# s2 = "silent" 
s1 = "aab"
s2="abb"
print(checkAnagram(s1,s2))

#Time complexity = Theta(n) 
# Auxilary Space = O(c) , where c is constant size of counter list
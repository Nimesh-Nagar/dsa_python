''' 
Leftmost Repeating Character

We are given a string s, we need to find out index of leftmost characters that is present in given string more than once.
If there is no character which is repeating , then we need to print -1.

For Example: Let us consider a string: str="abbcc", then our answer will be 1 because character 'b' is the leftmost character 
which is repeating in given string str.

'''

#-------------------------------------------
# METHOD 1 : Nave approch
#-------------------------------------------

def leftmost_repeat(str):
    
    for i in range(len(str)):
        for j in range(i+1, len(str)):
            if str[i] == str[j]:
                return i 
    return -1 

str = "ceabda"
print(leftmost_repeat(str))


#-------------------------------------------
# METHOD 2 : 
#-------------------------------------------

# check if srting is rotated ;

def areRotated(s1, s2):
    if len(s1) != len(s2):
        return False
    
    temp = s1 + s1
    
    # return temp.find(s2) != -1 
         # or
    return s2 in temp 

s1 = "ABAB" 
s2 = "ABBA" 
# s1 = "ABCD"
# s2 = "CDAB"

print(areRotated(s1,s2))
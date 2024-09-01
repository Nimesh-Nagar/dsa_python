# check if srting is rotated ;

def areRotated(s1, s2):
    if len(s1) != len(s2):
        return False
    
    temp = s1 + s1
    return temp.find(s2) != -1 

# s1 = "ABAB" 
# s2 = "ABBA" 
s1 = "ABDC"
s2 = "CDBA"

print(areRotated(s1,s2))
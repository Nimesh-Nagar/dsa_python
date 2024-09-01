'''
You are given a string s. You need to find if the string is a panagram or not.
A panagram contains all the letters of english alphabet at least once.
'''

#----------------------------------------------
# METHOD 1
#----------------------------------------------

def isPanagram(s):
    
    if (len(s) < 26):
        return False
    
    str = s.lower() #converting to lower case
    strList = list(str) # convering to list

    strSet = set() 
    strSet.update(strList) # converting into set
    
    if len(strSet) == 26:
        return True
    return False
        

# given_str = "gfhj"
given_str = "Thequickbrownfoxjumpsoverthelazydog"

print(isPanagram(given_str))

#----------------------------------------------
# METHOD 2 
#----------------------------------------------

string = "The quick brown fox jumps over a lazy dog"

check=[]

for ele in string.lower():
    if ele not in check and ele != ' ' and ele.isnumeric() == False:
        check.append(ele) 

print(f"Original String ---> {string}")

if len(check) == 26:
    print("String is Pangram")
else:
    print("String is NOT Pangram")

#----------------------------------------------
# METHOD 3 
#----------------------------------------------
def check(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for ele in alphabet:
        if ele not in string:
            return False
        else:
            return True
        
string = "The quick brown fox jumps over a lazy dog"

if (check(string)== True):
    print(" Pangram ")
else:
    print("Not Pangram")   



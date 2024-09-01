'''
You are given a string s. You need to find the missing characters in the string to make 
a panagram ( a sentence using every letter of english alphabet at least once ).
Note: The output characters will be lowercase and lexicographically sorted.

You only need to complete the function misssingPanagram() that takes s as parameter 
and returns -1 if the string is a panagram, 
else it returns a string that consists missing characters.

'''


def missing_Panagram(s):
    alphabets = set('abcdefghijklmopqrstuvwxyz')
    string = s.lower()

    missing = ''.join(sorted(alphabets - set(string))    )
        
    if missing:
        return missing
    else:
        return -1 
        
    
print(missing_Panagram(s="abcdefghijklmopqrstuvwxyz"))

def missingPanagram(s):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        missing_chars = ""
        s_lower = s.lower()
        for c in alpha:
            if c not in s_lower:
                missing_chars += c
        if not missing_chars:
            return -1
        return missing_chars
        
print(missing_Panagram(s="abcdefghijklmopqrsyz"))
'''
Reverse words in a given string
Let the input string be “i like this program very much”. 
The function should change the string to “much very program this like i”
'''

#-----------------------------------
# METHOD 1 
#-----------------------------------
org_str = "Welcome to dsa"
print(org_str)

# temp = org_str.split(" ")
# rev = temp[::-1]
# print(" ".join(rev))

print( " ".join(org_str.split(" ")[::-1]) )


print('-----------------------------------')
# METHOD 2
print('-----------------------------------')

def reverse_words(org_str, start, end):
    while start < end:
        org_str[start], org_str[end] = org_str[end], org_str[start]
        start += 1
        end -= 1

org_str = "I love programming"
# org_str = "Welcome to dsa"
print(org_str)

org_str = list(org_str)
start = 0 

while True:
    try:
        end = org_str.index(' ', start)
        reverse_words(org_str, start, end-1)
        start = end + 1
    
    except ValueError:
        reverse_words(org_str, start, len(org_str)-1)
        break

org_str.reverse()
org_str = "".join(org_str)
print(org_str)

# Q1 python program to find armstrong number or not (153 = 1^3 + 5^3 + 3^3 = 153)
''' 
list of armstrom number 
 1, 2, 3, 4, 5, 6, 7, 8, 9, 
 370,153, 370, 371, 407
 1634, 8208, 9474  
'''

# Function to calculate order of the number
def order(n):
    x = 0
    while n!=0:
        x = x + 1
        n = n // 10
    return x


# Function to check whether the given number is Armstrong number or not
def isAmstrong(num):
    x = order(num)
   
    check = num
    sum1 = 0  

    while check != 0:
        temp = check % 10
        sum1 = sum1 + temp**x
        check = check // 10

    if sum1 == num :
        print("Given Number is Armstrong ")
    else: 
        print("NOT an Armstrong Number ")        


num = int(input("\nEnter number to check it is Armstrong or Not : "))
isAmstrong(num)
# Print all divisor of a given number


def divisor(num):
    print("Nave Solution")
    i = 1
    while i <= num:
        if num % i == 0:
            print(i, end=" ")
        i += 1
    print("\n")


##################################
"""
If we look carefully, all the divisors are present in pairs. 
For example if n = 100, then the various pairs of divisors are: (1,100), (2,50), (4,25), (5,20), (10,10).
We, however, have to be careful if there are two equal divisors as in the case of (10, 10). 
In such case, we'd print only one of them. 
"""
##################################


def optimise_divi(num):
    print("optimised solution ")
    i = 1
    while i * i <= num:
        if num % i == 0:
            print(i)
            if i != num / i:
                print(int(num / i))

        i += 1


def optimise_divi2(num):
    print("\nSorted order")
    j = 1
    while j * j < num:  # divisor from 1 to (n)^1/2 . excluding (n)^1/2
        if num % j == 0:
            print(j)
        j += 1

    while j >= 1:  # divisor from (n)^1/2 to 1 . including (n)^1/2
        if num % j == 0:
            print(int(num / j))
        j -= 1


num = int(input("Enter Number to find all Divisor : "))
divisor(num)
optimise_divi(num)
optimise_divi2(num)

def sum_dig(n):

    if n == 0:         #or n < 10 for single digit values
        return n
    else:
        return sum_dig(n // 10) + (n % 10)
    

print(sum_dig(2))
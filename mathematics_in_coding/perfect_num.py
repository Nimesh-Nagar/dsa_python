def is_perfect_number(num):
    if num < 1:
        return False

    divisor_sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisor_sum += i

    return divisor_sum == num

# Input from user
num = int(input("\nEnter a number to check if it's perfect: "))

if is_perfect_number(num):
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")

    
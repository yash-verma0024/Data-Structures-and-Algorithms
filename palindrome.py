#Check whether the given number is palindrome or not
n = int(input("Enter the number : "))
num = n
result = 0     #Result (for comparing (Which is reverse of n)) is initially 0

while num > 0:
    last_digit = num % 10
    result = (result * 10) + last_digit
    num = num // 10

print("True" if result == n else "False")
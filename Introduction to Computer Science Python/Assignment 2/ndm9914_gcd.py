"""
This scripts takes two integers and returns the greatest common divisor

Submitted by Nicholas Meng, NetID ndm9914
The script asks the user to input two numbers, and if the second input is greater than the first input,
the script switches them so the first input is greater. Then, the script follows a loop inspired by the
Euclidean algorithm until the 'divisor' variable equals 0. The script returns the last non-zero value
that the divisor took on as the final answer.
"""
dividend = int(input("What is the first number? "))
divisor = int(input("What is the second number? "))
temp = 0
if dividend < divisor:
    temp = dividend
    dividend = divisor
    divisor = temp
dividend_initial = dividend
divisor_initial = divisor
while divisor != 0:
    temp = divisor
    divisor = dividend % divisor
    dividend = temp
print(f'gcd({dividend_initial}, {divisor_initial}) = {temp}')


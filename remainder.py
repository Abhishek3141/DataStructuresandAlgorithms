import math

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
quotient = num1 / num2
print(quotient)
roundedquotient =  math.trunc(quotient)
addnum = roundedquotient * num2
remainder = num1 - addnum
print(remainder)

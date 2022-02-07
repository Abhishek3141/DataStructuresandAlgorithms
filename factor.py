num = int(input("Enter the number you want to factor:"))
emptarr = []


for i in range(1,round((num)/2)):
    if num % i == 0:
        print(i)
        num2 = num/i
        print(num2)




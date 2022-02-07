def fibb(num):
    if num <= 1:
        return num
    else:
        return(fibb(num-1)+fibb(num-2))

val = 9
for i in range(val - 1):
    print(fibb(i))
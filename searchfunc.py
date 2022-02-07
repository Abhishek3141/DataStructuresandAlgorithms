arr = [3,3,5,7]
inpu1 = int(input("What number do you want to find?"))
oparr = []
for i in range(len(arr)):
    if inpu1 == arr[i]:
        a = i+1
        oparr.append(a)
        
    
print("Posiion in list:", oparr)
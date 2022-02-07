inputStr = input("Please enter your password:")
list = inputStr
pointsnum = 0
pointslet = 0
for i in range(len(list)):
    if list[i].isdigit():
       pointsnum = 1
    elif list[i].isalpha():
        pointslet = 1
    
    if pointsnum == 1 and pointslet == 1:
        print("valid password")
        break

if pointsnum != 1 or pointslet != 1:
    print("invalid password")
    

    

 
        

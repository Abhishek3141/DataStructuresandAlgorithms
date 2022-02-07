inputStr = input("Please enter a String:")
list = list(inputStr)
# for i in list:
#     print(i)
for i in range(len(list)):
    if list[i] == " ":
       list[i] = ""
list2 = ''.join(x for x in list)
print(list2)
inputStr = input("Please enter letters and numbers with a space in between: ")
replChar = input("What characters do you want to replace:")
replByChar = input("Wha do you want to replace it with:")

print(inputStr)
list = inputStr.split()
# for i in list:
#     print(i)
for i in range(len(list)):
    if list[i]==replChar:
        list[i] = replByChar
list2 = ' '.join(x for x in list)
print(list2)
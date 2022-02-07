inputStr = input("Type a String:")
inputList = list(inputStr)
length = round((len(inputList)/2))
inputlistlen = len(inputList)
temp = ""
for i in range(length):
    temp = inputList[i]
    inputList[i] = inputList[inputlistlen-(i+1)]
    inputList[inputlistlen-(i+1)] = temp
inputList = ''.join(x for x in inputList)
print(inputList)

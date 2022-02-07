inputStr = input("Type a sentence:")
inputList = inputStr.split()
outputList = list('')

for i in range(len(inputList)):
    outputList.append(inputList[len(inputList)-(i+1)])
outputList = ' '.join(x for x in outputList)
print(outputList)


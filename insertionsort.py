def insertionSort(array):
      for i in range(1, len(array)):
        x = array[i]
        j = i-1
        while j >=0 and x < array[j] :
                array[j+1] = array[j]
                j -= 1
        array[j+1] = x

array = [12, 11, 13, 5, 6]
insertionSort(array)
for i in range(len(array)):
    print(array[i])
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

#print(findSmallest([4,3,5,7,9,1,12]))

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        # find the smallest element in the array
        smallest = findSmallest(arr)
        # add it to the new array
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5,3,6,2,10]))

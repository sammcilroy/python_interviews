def recursive_maximum(arr, max=0):
    if arr == []:
        return max
    if arr[0] > max:
        max = arr[0]
    return recursive_maximum(arr[1:], max)

    

print(recursive_maximum([2,4,6], 0))
print(recursive_maximum([3,1,5,7,2,9,2]))

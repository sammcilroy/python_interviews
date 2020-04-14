def recursive_length(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1

    return 1 + recursive_length(arr[1:])


print(recursive_length([2,4,6]))
print(recursive_length([1,2,3,4,5,6,7,8,9,0]))

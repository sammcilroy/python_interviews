def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

#print(sum([2,4,6]))

def recursive_sum(arr):
    # BASE CASE - length of array is zero or 1
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    # RECURSIVE CASE - sum
    return arr[0] + recursive_sum(arr[1:])



#print(recursive_sum([]))

print(recursive_sum([2,4,6]))

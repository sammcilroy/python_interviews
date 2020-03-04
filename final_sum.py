def sum1(n):
    final_sum = 0

    for x in range(n+1):
        final_sum += x
    
    return final_sum

print(sum1(10)) #55

def sum2(n):
    return (n*(n+1))/2

print(sum2(10))


import timeit
timeit.timeit("sum1(100)")
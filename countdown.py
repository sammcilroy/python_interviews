#def countdown(i):
#    print(i)
#    countdown(i-1)

#countdown(10) # recursion, no base case, will run forever!

def countdown(i):
    print(i)
    if i <= 0: # BASE CASE
       return
    else: # RECURSIVE CASE
        return countdown(i-1)

countdown(10)


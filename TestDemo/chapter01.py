def function(n):
    if n < 0:
        return -1
    elif n == 1 or n == 2:
        return 1
    else:
        return function(n - 1) + function(n - 2)


result = function(30)
if result != -1:
    print(result)

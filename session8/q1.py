def myfun(x):
    if x == 0:
        return 1
    return x + myfun(x-1)
print(myfun(5))

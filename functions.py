def help():
    print("helper function")

def sum(a,b,c=0):
    return a+b+c
print(help())
print(help())
print(sum(5,3))
print(sum(5, 3, 2))
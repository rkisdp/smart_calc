def add(x, y):
    return(x + y)

def sub(x, y):
    return(x - y)

def mul(x, y):
    return(x * y)

def div(x, y):
    return(x / y)

def hcf(x, y):
    x, y = y, x % y
    return(x)

def lcm(x, y):
    if x>y:
        SmallNum = x
    else:
        SmallNum = y
    while True:
        if(SmallNum % x == 0 and SmallNum % y == 0):
            print(SmallNum)
            break
        SmallNum = SmallNum + 1
    return lcm

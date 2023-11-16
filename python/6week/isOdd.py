a = int(input())
b = int(input())

def isOdd(a, b):
    if(a and b) % 2 != 0:
        return True
    else:
        return False



print(isOdd(a,b))

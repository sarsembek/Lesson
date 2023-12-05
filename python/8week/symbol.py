def myfunc(symbol):
    return lambda a : a[0] == "h"

symbol = input()
txt = input()

x = myfunc(symbol)

print(x(txt))
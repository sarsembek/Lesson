def arithmetic(x,y,z):
    if z == "+":
        return x + y
    elif z == "-":
        return x - y 
    elif z == "*":
        return x * y
    elif z == "/":
        return x / y 
    else:
        return "Неизвестная операция"

x = int(input())
y = int(input())
z = input()

print(arithmetic(x,y,z))
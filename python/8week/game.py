import random

flag = True 

target = random.randint(1,100)

print("1-ден 100-ге дейін бір санды енгізіңіз:")

while flag:
    n = int(input())
    if n < 1 or n > 100:
        print("Саныңыз қате")
        n = int(input())
    elif n == target:
        print("Дұрыс жауап")
        flag = False
    elif n > target:
        print("Көп")
    elif n < target:
        print("Аз")
    else:
        continue


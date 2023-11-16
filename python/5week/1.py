n = int(input())

cnt = 0

def power(n,cnt):
    for i in range(n + 1):
        cnt += i**2
    return cnt

print(power(n,cnt))
print(power(n,cnt))
print(power(n,cnt))


n = int(input())

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: 
                return False
            else:
                return True

print(isPrime(n))
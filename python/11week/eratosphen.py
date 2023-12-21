def erotesphen(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for x in range(2, int(limit**0.5)):
        if is_prime[x]:
            primes.append(x)
            for y in range(x * x, limit + 1, x):
                is_prime[y] = False
    for x in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[x]:
            primes.append(x)
    return primes

result = erotesphen(10000)

n = int(input())

print(result[n - 1])


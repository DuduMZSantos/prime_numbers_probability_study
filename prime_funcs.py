from math import isqrt

def is_prime(n:int) -> bool:
    if n == 1:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

def naive_method(n:int) -> float:
    primes_count = 0
    for i in range(1,n+1):
        primes_count += int(is_prime(i))
    return primes_count / n

def optimized_method(n:int) -> float:
    no_primes = {1}
    for i in range(2,isqrt(n)+1):
        for aux in range(i, n//i + 1):
            no_primes.add(i*aux)
    return (n-len(no_primes))/n
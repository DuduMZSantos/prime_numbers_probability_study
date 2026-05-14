# Author
Eduardo Matte Zanardo dos Santos

# Introduction

The intention of this article analyses the efficiency of algorithms that answear the following questions:<br>

1. "Given a number N, what is the probability of a prime number to be randomly chosen in the interval [1,N]?"<br>
2. "How does the function of this probability depending on N look like?"<br>

In order to do that, the trivial solution is implemented as well as the optmized one, both of them will be explained and analyzed in the following sections.

# Trivial Solution

### Algorithm

The idea of the trivial solution is to iterate over all numbers from 2 to N and for each of them, check if it is prime. So, at the end of all iterations, the count of prime numbers divided by N will return the probability of a randomly chosen number in this range to be prime.

To find out whether a number X is prime, X shall be divided by all numbers from 2 until its integer half or until the rest of the division is zero. It is not necessary to divide X by a number greater than its half because the greatest divisor of a number, without considering the number itself, is its half.

### Pseudocode

The whole algorithm can be written by this:

```text
    function is_prime(n):
        if n == 1:
            return False
        for i in [2, n//2]:
            if n mod i == 0:
                return False
        return True

    primes_count <- 0
    for i in [1, N]:
        if is_prime(i):
            primes_count++
    
    probability <- primes_count / N
```

### Complexity Analysis

This algorithm iterates over all numbers in the interval between 1 and N and, for each of them, which will be called by auxiliar here for better understanding, iterates, in the worst case scenario, over aux divided by 2. This leads to a complexity of O(N*aux/2), which can be generalized for O(n²). In other words, this algorithms has a problem of scalability, because it is very slow when applied to a high value of N.

# Optimized Solution

### Algorithm
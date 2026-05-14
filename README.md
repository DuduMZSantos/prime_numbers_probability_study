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

To understand the optimized algorithm, it is necessary to keep in mind the principle that, in a multiplication, the order of the factors does not change the product. The idea of this algorithm consists in, instead of counting how many numbers between 1 and N are prime, saving all the non prime numbers between 1 and N, and then divide N - count of non prime numbers by N, using the complementary logic.

In order to do save all this non prime numbers, it is necessary to iterate over all the numbers between 2 and the integer square root of N, that will be called by i, and, for each i, it is made a new iteration over all the numbers between i and the integer division of N by i. The products of the multiplication of i and each of these numbers are added to the non prime list, which is initialized with only the number 1, if and only if this product is not in the list yet.

However, it is very important to understand why it is possible to start the second iteration by the number itself, eg: 4\*4, 4\*5, 4\*6 and so on. As mentioned in the first paragraph, the order of the factors does not change the product. Because of that, using the same example, it is not necessary to do 4\*2 and 4\*3, because 2\*4 and 3\*4 were already calculated in the iterations of 2 and 3. For the same reason, the first iteration can be stopped at the integer square root of N because, if we are starting the second iteration by the same current number of first iteration, the greatest number that can be multiplied by itself without exceeding N is the integer square root of N.

### Pseudocode

The whole algorithm can be written as following:

```text
    non_primes <- [1]
    for n in [2, integer(√N)]:
        for aux in [n, N/n]:
            product <- n * aux
            if product not in non_primes:
                non_primes <- non_primes + [product]
    
    probability <- (N-length(non_primes)) / N
```

### Complexity Analysis

This algorithm iterates over all numbers between 2 and the integer square root of N and, for each of these numbers, called by auxiliar for better understanding, iterates over all numbers between auxiliar and the integer division of N by auxiliar. In other words, it can be described as O((N√N)/aux - aux√N), which can be generalized for O(N√N).

# Probabilities Function

In order to obtain the shape of the probabilities function, all the results of the optimized algorithm from N going from 2 untill 5000 and plotted in a line graph. It is show in the file results.png.

# Conclusion

This study has implemented successfully a more scalable algorithm for the problem of the probability of a random number chosen between 1 and a given N to be prime. Besides that, the code provides the shape of the equation of these probabilities in function of N. All the results are shown in the file results.png.
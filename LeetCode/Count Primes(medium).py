# Given an integer n, return the number of prime numbers that are strictly less than n.

 

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0


def countPrimes(n: int) -> int:
        
        #Initial Edge Cases (0, 1 non-prime by definition)
        
        if n <= 2:
            return 0
        
        #population of list for classification of primes
        #all numbers initialized as prime, and then discounted via 'Sieve of Eratosthenes' algorithm
        #naturally, our list is of size(n)

        primes = [True] * n
        primes[0] = primes[1] = False 
        
        #for all elements in the range [2 , n)
        for number in range(2, n):
            
            #if it is a prime 
            if primes[number]:
                
                #starting from 2 * prime and ending at n - in increments of prime
                for multiple in range(2 * number, n, number):
                    
                    
                #change index accounting for prime validity to 'False' or every multiple of found prime.
                #we can correctly categorize a large number of composite numbers due to the fact that our first 
                #prime is undoubtly a factor of all larger multiples of the same number.

                    primes[multiple] = False
                    
        #Sum of Total Booleans             
        return sum(primes)
        

print(countPrimes(10))
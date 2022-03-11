#Ariel Tynan
#Euler Problem 058, Spiral primes, Solved in Python
#Started 8 March 2022. Solved 11 March 2022

import numpy
from math import sqrt, ceil

#Prime number sieve used in previous problems, including Euler_050_Py
def prime_Sieve(n): #Function modified from Geeksforgeeks
     
    primes = [] # initial empty list of primes
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    for p in range(n + 1):
        if prime[p] and p != 2:
            primes.append(p)
    return primes

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(int(n/3 + (n%6==2)), dtype=numpy.bool)
    for i in range(1,int(int(n**0.5)/3+1)):
        if sieve[i]:
            k=int(3*i+1|1)
            sieve[int(k*k/3)::2*k] = False
            sieve[int(k*(k-2*(i&1)+4)/3)::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

#Problem range n
n = 1200000000 #max primes capable by computer

prime_list = primesfrom2to(n) #faster prime sieve
tot_checks = 1 #total corners checked
primes = 0
ratio = 1 #running decimal of primes to non primes
solved = False
while solved == False:
    for i in range(1,120000,2): #increments for every diameter i up to 119999
        for j in range(1,5):
            tot_checks = tot_checks + 1
            temp = i*i + j*(i+1)
            #print(temp)
            if temp in prime_list:
                primes = primes + 1
                #print(temp)
        if primes/tot_checks < ratio:
            ratio = primes/tot_checks
            print(i+2,primes, tot_checks, ratio) 
        if primes/tot_checks < .1 and i > 3:
            print("SOLVED:",i+2,temp,primes/tot_checks)
            solved = True
            break
                
                

    




#Pattern
# 1 3 5 7 9 13 17 21 25

# 17 16 15 14 13
# 18 05 04 03 12
# 19 06 01 02 11 
# 20 07 08 09 10
# 21 22 23 24 25







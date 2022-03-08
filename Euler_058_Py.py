#Ariel Tynan
#Euler Problem 058, Spiral primes, Solved in Python
#Started 8 March 2022

from numpy import sqrt

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
        if prime[p]:
            primes.append(p)
    return primes

#Problem range n
n = 10000000

prime_list = prime_Sieve(n)
#print(prime_list)
ratio = 1

#Create spiral
dia = 1 #diameter of square
tot_checks = 0 #total corners checked
primes = 0
for i in range(1,n):
    if i == dia*dia or i == dia*dia + (dia + 1) or i == dia*dia + 2*(dia + 1) or i == dia*dia + 3*(dia + 1):#check for corner
        tot_checks = tot_checks + 1
        #print(i)
        if i in prime_list:
            primes = primes + 1
        if i == dia*dia + 3*(dia + 1) and i != 1:
            dia = dia + 2

    #if i % 2 == 1 and sqrt(i).is_integer() and i != 1:
    #    dia = dia + 2
     #   #print(i,dia)
     #   tot_checks = tot_checks + 1
        
    
    if primes/tot_checks < ratio and i > 30:
        ratio = primes/tot_checks
        print(ratio)
        if ratio < 0.1:
            print(i,dia, ratio)
            break





# 17 16 15 14 13
# 18 05 04 03 12
# 19 06 01 02 11 
# 20 07 08 09 10
# 21 22 23 24 25







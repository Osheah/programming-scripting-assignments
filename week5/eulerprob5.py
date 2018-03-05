#Helen O'Shea 21/2/18
#Euler Problem 5 https://projecteuler.net/problem=5
#solution is 232792560 from here https://www.w3resource.com/euler-project/euler-problem5.php
n=2520*11 # 2520 is divisable by 10 factorial and 11 is prime

factors=range(10,21) # 1-10 found already
while n>1:
  for f in factors: 
    if n%f!=0: # if there is a remainder for n divided by f then it cannot be a factor
      break # not a factor so next f
  if ((f==20) and (n%f==0)): # if we get to this line then all the f's up to and including 20 - the max factor, divide with no remainder.
      ans=n
      n=0 # reset n so that the condition n>1 fails and the loop ends.
  n=n+1  #increase n till loop fails
print(ans) # ans = 232792560
#program takes a long time to run and would be faster if prime factorization was used

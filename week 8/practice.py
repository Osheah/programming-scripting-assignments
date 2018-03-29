#python fundamentals helen o'shea 19/3/2018 https://learnonline.gmit.ie/pluginfile.php/347931/mod_resource/content/1/problems.pdf
#1
def sumultiply(x,y):
  total=0
  for i in range(y):
    total = total + x
  return total
'''print(sumultiply(11,13))
print(sumultiply(5,123))'''
#2

def palindrome(s):
  ans= True 
  for i in range(len(s)):
    if s[i]!=s[len(s)-1-i]: 
      ans = False
  return ans

'''print(palindrome('radar'))
print(palindrome('10000011'))'''
#3
def simpleinterest(p,r,t):
  ans=p+p*t*r/100
  return ans
'''print(simpleinterest(1000,3,5))
print(simpleinterest(1000,7,10))  '''
#4
def compoundinterest(p,r,t):
  ans = p*(1+r/100)**t
  return ans
'''  
print(compoundinterest(1000,3,5))
print(compoundinterest(1000,7,10))'''
#5
def newtonsroot(n):
  r=n/2
  while r*r!=n:
    r=r-(r**2-n)/(2*r)
  return r
'''print(newtonsroot(100))
print(newtonsroot(144)) # still have to do it to 6 dp'''
#6
def pitondecs(n):
  import math
  ans = round(math.pi,n) # had to look up round and math pi
  return ans
'''print(pitondecs(2))
print(pitondecs(6))'''
#7
def etondecs(n):
  import math
  ans = round(math.e,n) #same as 6
  return ans
'''print(etondecs(2))
print(etondecs(6))'''
#8
def caesar(s, n):
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']#simplify it first by using lower case
for i in s: 
  range(len[i] = range(len[i]+n%26)
print(alpha)

#return s
 
characters only
#print(caesar('abcd', 3))  
#print(caesar('Hello, World!', 2)) # not done
'''
#9
def sortlist(l):
  for i in range(l): 
    if i
#10
def countstr(s):'''

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
def simpleinterest(p,t,r):
  ans=p+p*t*(r/100)
  return ans
print(simpleinterest(1000,3,5))
print(simpleinterest(1000,7,10))  
# Helen O'Shea uploaded on the 6/2/18
# Adapted from Ian McLoughlin's code https://github.com/ianmcloughlin/python-fib/blob/master/fibname.py
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0 # initialize variables
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "O'Shea" # my surname
first = name[0] # take the first element of o'shea i.e. O
last = name[-1] # take the last element of o'shea i.e. a
firstno = ord(first) # get the unicode character integer of O 
lastno = ord(last) # get the unicode character integer of a
x = firstno + lastno

ans = fib(x) # return the xth fibonacci number
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

# week 2 forum comments My surname is O'Shea
#The first letter O is number 79
#The last letter a is number 97
#Fibonacci number 176 is 2706074082469569338358691163510069157
#ord returns the unicode for the string it represents. eg. "Given a string representing one Unicode character, return an integer
#representing the Unicode code point of that character.  For example,
#ord('a') returns the integer 97 and ord('€') (Euro sign)
#returns 8364.  This is the inverse of chr(). " -  source https://docs.python.org/3/library/functions.html#ord

#comments is found on forum here https://learnonline.gmit.ie/mod/forum/discuss.php?d=11151
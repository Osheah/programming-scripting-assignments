# Helen O'Shea uploaded on the 6/2/18
# Adapted from Ian McLoughlin's code https://github.com/ianmcloughlin/python-fib/blob/master/fibname.py
# Ian McLoughlin
# A program that displays Fibonacci numbers.

def fib(n): # define function
  """This function returns the nth Fibonacci number."""
  i = 0 # initalize variables
  j = 1  # initalize variables
  n = n - 1

  while n >= 0: # while n is a non negative integer
    i, j = j, i + j # i = j and j = i+j
    n = n - 1 # update n
  
  return i 

# Test the function with the following value.
x = 22 # H = 8th letter of alphabet N= 14th letter of alphabet 8+14 = 22
ans = fib(x)
print("Fibonacci number", x, "is", ans)


# comments on the forum 
# week 1 forum comments My name is Helen, so the first and last letter of my name (H + N = 8 + 14) give the number 22. The 22nd Fibonacci number is 17,711.
# https://learnonline.gmit.ie/mod/forum/discuss.php?d=10326


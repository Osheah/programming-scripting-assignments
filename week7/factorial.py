# Helen O'Shea 5/3/2018
# Write a Python script containing a function called factorial() that takes a single input/argument which is a positive integer and returns its factorial. The factorial of a number is that number multiplied by all of the positive numbers less than it. For example, the factorial of 5 is 5x4x3x2x1 which equals 120. You should, in your script, test the function by calling it with the values 5, 7, and 10.

def factorial(n):
  if n==1: 
    return 1
  elif n==0: 
    return 0
  else: 
    fac=1
    for i in range(1, n+1):
      fac=fac*i
  return fac
print('5 factorial is ',factorial(5),'\n' '7 factorial is ', factorial(7), '\n' '10 factorial is ', factorial(10))

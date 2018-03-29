# Helen O'Shea 5/3/2018
# Write a Python script containing a function called factorial() that takes a single input/argument which is a positive integer and returns its factorial. The factorial of a number is that number multiplied by all of the positive numbers less than it. For example, the factorial of 5 is 5x4x3x2x1 which equals 120. You should, in your script, test the function by calling it with the values 5, 7, and 10.

def factorial(n): # define function
  if n==1: # if n = 1 then 1 factorial is 1
    return 1
  elif n==0: # if n is 0 then 0 factorial is 0
    return 0
  else: # n is not 1 or 0
    fac=1 # initalise data
    for i in range(1, n+1): # for i in [1 to n+1)
      fac=fac*i # muptiply factorial by i
  return fac
print('5 factorial is ',factorial(5),'\n' '7 factorial is ', factorial(7), '\n' '10 factorial is ', factorial(10)) # check the calc via n = 5,7,10

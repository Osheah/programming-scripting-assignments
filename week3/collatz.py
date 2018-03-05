# Helen O'Shea, 2018-02-06
# Collatz conjecture: https://en.wikipedia.org/wiki/Collatz_conjecture
x = int(input('Enter a positve integer: '))

# When end state of 1 not reached perform multiply by 2 if even and multiply by 3 plus add 1 if odd.

while x >1:
  if (x % 2 == 0):
    x = int(x / 2)  
    print(x)
  else: 
    x = int((3 * x) + 1)
    print(x)

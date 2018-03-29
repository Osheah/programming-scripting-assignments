#Helen O'Shea 27/02/2018 week 6 exercises
# Exercise 5k=: Write a Python script that reads the Iris data set in and prints the four numerical values on each row in a nice format. That is, on the screen should be printed the petal length, petal width, sepal length and sepal width, and these values should have the decimal places aligned, with a space between the columns.
# data taken from http://archive.ics.uci.edu/ml/machine-learning-databases/iris/
with open("data/iris.csv") as f:
  header='sl    sw    pl    pw' # sl = sepal length in cm; sw = sepal width in cm pl = petal length in cm pw= petal width in cm attributes taken from http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names
  print(header) # print out the header
  for line in f: 
    data=line.split(',')[0:4]#split the lines at the comma for the first four entries
    if len(data)==4: # needed to not print out the '/n' at the end
      print('{:2s}'.format(data[0]),' ','{:2s}'.format(data[1]),' ', '{:2s}'.format(data[2]),' ', '{:2s}'.format(data[3])) # format the data to 2 digits

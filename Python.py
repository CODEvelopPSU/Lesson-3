#####################################################
#           Examples with Python for loops          #
#####################################################
#Food list example
edibles = ["chicken nuggets", "fries", "pastas", "oranges"]

for food in edibles:
  if food == "oranges":
    print("I only want unhealthy food")
  else:
    print("That's better")
print("")
#####################################################
#Pythagorean theorem example
from math import sqrt

n = int(input("Type the maximum number that you want."))

for a in range(1, n + 1):
  for b in range(a, n):
    c_square = a**2 + b**2
    c = float(sqrt(c_square))
  if((c_square - c**2) == 0):
    print(a, b, c)
  else:
    print(a, b, c)
print("")
#####################################################
#colors list example
colors = ["blue"]

for i in colors:
  if i == "blue":
    colors += ["white"]
  elif i == "white":
    colors += ["grey"]
print(colors)
print("")
#####################################################
#making methods example
def for_loop():
  for number in range(20):
    sum = 3 + 156
    print(sum)

for_loop()
print("")
#####################################################
#Sideways pyramid example
n = 5
for i in range(n):
  for j in range(i):
    print('* ', end = "")
  print(' ')

for i in range(n, 0, -1):
  for j in range(i):
    print('* ', end = "")
  print('')
#####################################################


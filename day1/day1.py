import math

# Task 1
def fuel_required(mass):
  return math.floor(mass/3)-2

# Task 2
def fuel_required_recursive(mass):
  sum = 0
  while fuel_required(mass) > 0:
    mass = fuel_required(mass)
    sum += mass
  return sum

f = open("input.txt", "r")
task1 = 0
task2 = 0

for x in f:
  task1 += fuel_required(int(x))
  task2 += fuel_required_recursive(int(x))

print("Task 1 answer: " + str(task1))
print("Task 2 answer: " + str(task2))
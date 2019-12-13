import math

def get_wires():
  f = open("input.txt", "r")
  wires = []
  line = f.readline()
  while line:
    wires.append(line.strip().split(","))
    line = f.readline()
  return wires

def possible_coords(wire):
  x = 0
  y = 0
  steps = 0
  coords = {}

  for i in range(len(wire)):
    for j in range(int(wire[i][1:])):
      if wire[i][0] == 'U':
        y += 1
      elif wire[i][0] == 'D':
        y -= 1
      elif wire[i][0] == 'R':
        x += 1
      elif wire[i][0] == 'L':
        x -= 1
      steps += 1
      if (x,y) not in coords:
        coords[(x,y)] = steps
  return coords

def point_distance(x, y):
  return abs(x) + abs(y)

wires = get_wires()

wire_1 = possible_coords(wires[0])
wire_2 = possible_coords(wires[1])

intersections = wire_1.keys() & wire_2.keys()

distance = [point_distance(x, y) for (x, y) in intersections]
print(min(distance))

steps = [wire_1[steps] + wire_2[steps] for steps in intersections]
print(min(steps))


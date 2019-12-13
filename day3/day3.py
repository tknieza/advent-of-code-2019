f = open("input.txt", "r")

instructions = []
line = f.readline()
while line:
  instructions.append(line.strip().split(","))
  line = f.readline()

print(instructions)
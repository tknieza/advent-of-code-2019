def meet_criteria_part1(num):
  num_str = str(num)

  if len(num_str) != 6:
    return False

  success = False

  for i in range(len(num_str)-1):
    if int(num_str[i]) > int(num_str[i+1]):
      return False
    if num_str[i] == num_str[i+1]:
      success = True

  return success

def meet_criteria_part2(num):
  num_str = str(num)

  if len(num_str) != 6:
    return False

  success = False

  for i in range(len(num_str)-1):
    if int(num_str[i]) > int(num_str[i+1]):
      return False

  i = 0
  while i < len(num_str) - 1:
    match = 0
    while i < len(num_str) - 1 and num_str[i] == num_str[i+1]:
      match += 1
      i += 1
    if match == 1:
      success = True
    i += 1

  return success

total = [0, 0]

for i in range(130254, 678275):
  if meet_criteria_part1(i):
    total[0] += 1
  if meet_criteria_part2(i):
    total[1] += 1

print(total[0])
print(total[1])
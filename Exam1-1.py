# Sum sq using for loop

def sum_sq(number):
  sum = 0
  for num in range(number+1):
    sum = sum + (num * num)
  return sum


print(sum_sq(10))



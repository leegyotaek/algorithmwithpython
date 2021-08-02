# 1. Sum sq using for loop

def sum_sq(number):
  sum = 0
  for num in range(number+1):
    sum = sum + (num * num)
  return sum

def sum_sq2(number):
  return number * (number+1) * (2*number + 1)


# print 1*1 + 2*2 + 3*3 + 4*4....+ 10*10
print(sum_sq(10))
print(sum_sq2(10))



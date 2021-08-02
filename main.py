# 1. Sum sq using for loop

def sum_sq(number):
  sum = 0
  for num in range(number+1):
    sum = sum + (num * num)
  return sum

def sum_sq2(number):
  return number * (number+1) * (2*number + 1) / 6


# print 1*1 + 2*2 + 3*3 + 4*4....+ 10*10
print(sum_sq(10))
print(sum_sq2(10))


# 2. find max num out of list
def find_max(l):
  max_num=l[0]
  print('max_nu : '+str(max_num))
  n = len(l)

  for i in range(n):
    if(l[i] > max_num):
      max_num = l[i]
  
  return max_num

print(find_max([11,3,34100,111,10000,10001]))
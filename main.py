# Given n as input. Print sum of cube of all numbers from 1 to n.

n = 4
cube = 0
sum = 0
for i in range(1,n+1):
  cube = i*i*i
  sum = sum + cube
print(sum)

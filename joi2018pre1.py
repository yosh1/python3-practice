import math
a,b,c = map(int,input().split())
answer = 0
count = 0
day = 0
while c > 0:
  c = c - a
  day = day + 1
  count = count + 1
  if count == 7:
    c = c - b
    count = 0
print(day)
/Users/yoshi1125hisa/Vagrant/ubuntu64_16/workspace/python3-competition-programming/main2.py

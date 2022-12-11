import time
import sys
x1 = time.time()
n= 10000
r= 0.0
for i in range(1, n+1):
    for j in range(1, n+1):
        r+=1/i/j
print(r)
x2= time.time()
print(x2-x1)

fred = int(sys.stdin.readline())


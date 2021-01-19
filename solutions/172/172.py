n = 5

from math import log
arr = []
answer = 0
for i in range(1,int(log(n)/log(5)+1)):
    arr.append(5**i)
for j in range(len(arr)):
    answer += n//arr[j]
print(answer)
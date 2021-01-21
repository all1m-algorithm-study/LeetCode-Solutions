A = [-1,-1]
B = [-1, 1]
C = [-1, 1]
D = [ 1,-1]

dicA = {}
dicB = {}
dicC = {}
dicD = {}

for i in A:
    if i in dicA.keys():
        dicA[i] += 1
    else:
        dicA[i] = 1;
for i in B:
    for j in dicA.keys():
        if i+j in dicB:
            dicB[i+j] += dicA[j]
        else:
            dicB[i+j] = dicA[j]

for i in C:
    if i in dicC.keys():
        dicC[i] += 1
    else:
        dicC[i] = 1;
for i in D:
    for j in dicC.keys():
        if i+j in dicD:
            dicD[i+j] += dicC[j]
        else:
            dicD[i+j] = dicC[j]

ans = 0;
for i in dicD.keys():
    if -i in dicB.keys():
        ans += dicB[-i]*dicD[i]
print(dicB)
print(dicD)
print(ans)

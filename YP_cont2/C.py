n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

SA = set(A)
SB = set(B)
SC = set(C)

E = SA & SB & SC

deletions = 0

for i in range(n):
    if A[i] in E and B[i] in E and C[i] in E:
        continue
    else:
        deletions +=1

print(deletions)
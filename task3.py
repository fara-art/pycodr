N = int(input())

A = float(input())
B = float(input())
C = 0

for D in range(2, N):
    E = float(input())

    if C == 0 and not ((B > A and B > E) or (B < A and B < E)):
        C = D

    A = B
    B = E

print(C)

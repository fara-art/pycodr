N = int(input())

A = 1
B = 1

while B <= N:
    C = A + B
    A = B
    B = C

print(B)

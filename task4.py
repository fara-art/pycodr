N = int(input())

A = 0
B = 1

while B * 3 <= N:
    B = B * 3
    A = A + 1

print(A)

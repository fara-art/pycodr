A = float(input())
N = int(input())

B = A
C = 1
D = 1
E = A

for F in range(1, N + 1):
    C = C * (2 * F - 1)
    D = D * (2 * F)
    E = E * A * A
    B = B + C * E / (D * (2 * F + 1))

print(B)

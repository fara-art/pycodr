A = float(input())
B = float(input())

C = 1
D = A
E = A

while E <= 5:
    D = D + D * B / 100
    E = E + D
    C = C + 1

print(C)

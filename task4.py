n = int(input())

k = 0
power = 1

while power * 3 <= n:
    power = power * 3
    k = k + 1

print(k)

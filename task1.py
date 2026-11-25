n = int(input())

first = 1
second = 1

while second <= n:
    next_number = first + second
    first = second
    second = next_number

print(second)

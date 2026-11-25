x = float(input())
p = float(input())

day = 1
distance = x
total = x

while total <= 5:
    distance = distance + distance * p / 100
    total = total + distance
    day = day + 1

print(day)

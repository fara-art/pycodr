n = int(input())

left = float(input())
middle = float(input())
answer = 0

for position in range(2, n):
    right = float(input())

    if answer == 0:
        if not (middle > left and middle > right) and not (middle < left and middle < right):
            answer = position

    left = middle
    middle = right

print(answer)

x = float(input())
n = int(input())

answer = x
odd_product = 1
even_product = 1
x_power = x

for k in range(1, n + 1):
    odd_product = odd_product * (2 * k - 1)
    even_product = even_product * (2 * k)
    x_power = x_power * x * x
    answer = answer + odd_product * x_power / (even_product * (2 * k + 1))

print(answer)

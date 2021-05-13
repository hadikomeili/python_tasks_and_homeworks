# Print Pascal's Triangle

n = int(input('enter a number:'))

for i in range(1, n + 1):
    x = 1
    for j in range(1, i + 1):
        print(x, end=' ')
        x = (x * (i - j)) // j
    print()
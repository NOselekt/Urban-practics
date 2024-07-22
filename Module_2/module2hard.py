left_number = int(input())
result = ''

for i in range(1, left_number // 2 + 1):
    for j in range(i, left_number):
        if left_number % (i + j) == 0 and i != j:
            result += str(i) + str(j)

print(result == '118217316415514613712811910')


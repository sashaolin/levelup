number = int(input())
b = 1
while b > number:
    b *= number
    number += 1
print(b)

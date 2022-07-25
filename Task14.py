# Задайте натуральное число N. Напишите программу,
# которая составит список простых делителей числа N.
# (1 - составное число)

print()
def div(num):
    a = []
    i = 2
    while i <= num:
        if num % i == 0:
            b = 0
            j = 2
            while j < i:
                if i % j == 0:
                    b += 1
                j += 1
            if b == 0:
                a.append(i)
        i += 1
    return a

number = int(input("Введите число: "))
print(div(number))
# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

print()
def uniq(num):
    x = 0
    a = list(num.split())
    b = []
    i = 0
    while i < len(a):
        x = a[i]
        c = 0
        for j in range(len(a)):
            if int(a[j]) == int(x):
                c += 1
        if c < 2:
            b.append(int(x))
        i += 1
    return b

numbers = input('Введите числа через пробел: ')
print(f'Неповторяющиеся числа среди введённых вами являются: {uniq(numbers)}')
# Вычислить число c заданной точностью d
# Пример:
# - при d = 3, π = 3.141

print()
def pi(num):
    i = 1
    a = 3
    b = 1
    c = 12**0.5
    d = ''
    while i < 10000:
        if i % 2 != 0:
            b = b - (1/(a*(3**i)))
        else:
            b = b + (1/(a*(3**i)))
        a += 2
        i += 1
    c *= b
    c = str(c)
    for i in range(num+2):
        d += str(c[i])
    return float(d)

d = int(input("Введите число: "))
while d < 1 or d > 15:
    d = int(input("Введите число от 1 до 16: "))
print(pi(d))
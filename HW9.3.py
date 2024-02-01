nums = list(map(int, input("Введите числа через пробел: ").split()))
chit = set()
for i in nums:
    if i in chit:
        print("Yes")
    else:
        print("No")
    chit.add(i)

# А что не так ?
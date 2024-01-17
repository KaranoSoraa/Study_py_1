nums = list(map(int, input("Введите числа через пробел: ").split()))
for i in nums:
    che = nums.count(i)
    if che > 1:
        print(f"Для числа {i}: Yes")
    else:
        print(f"Для числа {i}: No")

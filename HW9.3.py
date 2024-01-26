nums = list(map(int, input("Введите числа через пробел: ").split()))
chit = []
for i in nums:
    if i == nums[0]:
        continue
    if i in chit:
        print("Yes")
    else:
        print("No")
    chit.append(i)
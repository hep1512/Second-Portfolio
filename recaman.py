nums = []
length = int(input())
a = 0
for i in range(0, length):
    if ((a - i) > 0) and (a - i) not in nums:
        a = a - i
    else:
        a = a + i
    nums.append(a)
print(nums)

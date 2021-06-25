nums = []

for i in range(2, 1000000):
    s = sum([int(x)**5 for x in str(i)])
    if i == s:
        nums.append(i)

print(nums)
print(sum(nums))

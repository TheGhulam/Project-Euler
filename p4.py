# class BreakIt(Exception): pass
max_so_far = 0

for i in range(999, 1, -1):
    for j in range(999, 1, -1):
        p = i*j
        p_str = str(p)
        if p_str == p_str[::-1]:
            if p > max_so_far:
                max_so_far=p
            else:
                pass
print(max_so_far)

# except BreakIt:
#     pass

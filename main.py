def get_sum(a,b):
    a, b = min(a, b), max(a, b)
    sum = a
    while a < b:
        a += 1
        sum += a
    return sum


print(get_sum(-1, 2))

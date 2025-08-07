def shell_sort(a):
    g = len(a) // 2
    while g:
        for i in range(g, len(a)):
            while i >= g and a[i] < a[i - g]:
                a[i], a[i - g] = a[i - g], a[i]
                i -= g
        g //= 2
    return a

print(shell_sort([12, 34, 54, 2, 3]))

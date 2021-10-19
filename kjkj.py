while True:
    Z = list(map(int,input().split()))
    if len(Z)==0:
        break
    i = (Z[0])
    j = (Z[1])
    if not Z:
        break
    else:
     max_length = 0
     for n in range(i, j+1):
        cycle = []
        while (True):
            cycle.append(n)
            if (n == 1):
                break
            if (n % 2 == 0):
                n = n // 2
            else:
                n = (3 * n) + 1
        if (max_length < len(cycle)):
            max_length = len(cycle)
     print(max_length)
    continue
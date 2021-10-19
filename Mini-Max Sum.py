arr=map(int,input().split())
arr_sorted = sorted(arr)
# print(arr_sorted[-4:])
print(sum(arr_sorted[:4]), sum(arr_sorted[-4:]))

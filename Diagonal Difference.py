n= int(input())
difference = 0
for i in range(n):
    row = input().split()
    # # print(row[i])
    # print(row[n-1-i])
    difference += (row[i] - row[n-1-i])
print (abs(difference))
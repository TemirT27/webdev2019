m = int(input())

arr = [a for a in input().split()][:m]

for x in range(0, m):
    if (x % 2 == 0):
        print(arr[x], end=' ')

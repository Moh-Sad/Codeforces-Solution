n = int(input())
items = list(map(int, input().split()))
ave = sum(items) / n
count = 0
for i in range(n):
    if items[i] == ave:
        count += 1
print(count)
for i in range(n):
    if items[i] == ave:
        print(i + 1, end=" ")
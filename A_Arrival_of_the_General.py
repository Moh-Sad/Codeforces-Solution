"""          Author: Mohammed Sadik
             Language: Python 3
             Difficulty: Easy              """
n = int(input())
items = list(map(int, input().split()))
first = max(items)
last = min(items)
p1 = 1
p2 = n
start = n
end = 1
for i in range(n):
    if items[i] == first and i + 1 <= start and items[0] != first:
        p1 = i + 1
        start = i + 1
    if items[i] == last and i + 1 >= end and items[n -1] != last:
        p2 = i + 1
        end = i + 1
ans = (p1 - 1) + (n - p2)
if p1 > p2:
    print(ans - 1)
else:
    print(ans)
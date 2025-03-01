"""
Author: Mohammed Sadik
Language: Python 3
Difficulty: Easy
"""

n = int(input())
items = list(map(int, input().split()))
items.sort()
count = 0
r = -1
collect = 0
for i in range(n):
    if collect > (sum(items) - collect):
        break
    else:
        collect += items[r]
        r -= 1
        count += 1
print(count)
"""              Author: Mohammed Sadik
                 Language: Python 3
                 Difficulty: Medium              """

n = int(input())
count = 1
items = []
for i in range(n):
    items.append(input())
for i in range(1, n):
    if items[i - 1]  != items[i]:
        count += 1
print(count)

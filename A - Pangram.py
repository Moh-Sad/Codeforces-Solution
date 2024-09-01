"""              Author: Mohammed Sadik
                 Language: Python 3
                 Difficulty: Medium                """

num = int(input())
check = list("abcdefghijklmnopqrstuvwxyz")
items = input().lower()
items = sorted(items)
found = []
for i in range(num):
    if items[i] not in found:
        found.append(items[i])
found = found[:26]
for i in range(num):
    if found == check:
        condition = True
    else:
        condition = False
if condition is True:
    print("YES")
else:
    print("NO")

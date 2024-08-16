"""          Author: Mohammed Sadik
             Language: Python 3
             Difficulty: Easy          """

n = int(input())
count = 0
for i in range(n):
    items = input().split()
    if int(items[0]) and int(items[1]) == 1:
        count += 1
    elif int(items[1]) and int(items[2]) == 1:
        count += 1
    elif int(items[0]) and int(items[2]) == 1:
        count += 1
print(count)

"""            Author: Mohammed Sadik
               Language: Python 3
               Difficulty: Easy            """

num, max = map(int, input().split())
items = input().split()
count = 0
for i in range(num):
    if int(items[i]) == 0:
        continue
    elif int(items[i])  >= int(items[max - 1]):
        count += 1
print(count)

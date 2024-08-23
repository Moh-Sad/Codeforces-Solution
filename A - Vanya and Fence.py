"""            Author: Mohammed Sadik
               Language: Python 3
               Difficulty: Easy              """

num, height = map(int, input().split())
items = input().split()
count = 0
for i in range(num):
    if int(items[i]) > height:
        count += 2
    else:
        count += 1
print(count)

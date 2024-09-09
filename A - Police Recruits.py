"""             Author: Mohammed Sadik
                Language: Python 3
                Difficulty: Easy               """

num = int(input())
items = list( map(int, input().split()))
count = 0
police = 0
for i in range(num):
    if items[i] > 0:
        police += items[i]
    if police <= 0 :
        count += 1
    if items[i] == -1 and police > 0:
        police -= 1
print(count)

"""             Author: Mohammed Sadik
                Language: Python 3
                Difficulty: Easy               """

p, min = map(int, input().split())
count = 0
for i in range(1, p + 1):
    min += i * 5
    if min <= 240:
        count += 1
    else:
        break
print(count)

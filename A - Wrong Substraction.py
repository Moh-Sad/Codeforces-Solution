"""          Author: Mohammed Sadik
             Language: Python 3
             Difficulty: Easy              """

value, num = map(int, input().split())
for i in range(num):
    if value % 10 == 0:
        value = value / 10
    else:
        value -= 1
print(int(value))

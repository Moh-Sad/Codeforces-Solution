"""Author: Mohammed Sadik
Language: Python 3
Difficulty: Easy"""

num = int(input())
count = 0
while num > 0:
    if num >= 100:
        num -= 100
        count += 1
    elif num < 100 and num > 19:
        num -= 20
        count += 1
    elif num < 20 and num > 9:
        num -= 10
        count += 1
    elif num < 10 and num > 4:
        num -= 5
        count += 1
    else:
        num -= 1
        count += 1
print(count)

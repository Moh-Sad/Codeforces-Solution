"""          Author: Mohammed Sadik
             Language: Python 3
             Difficulty: Easy            """

n = input().split()
num = n[0]
max = n[1]
count = 0
final = int(max) * int(num)
while True:
    if final % 2 != 0:
        final -= 1
    if final % 2 == 0 and final != 0:
        count += 1
    final = final - 2
    if final <= 0:
        break
print(count)

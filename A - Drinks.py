"""              Author: Mohammed Sadik
                 Language: Python 3
                 Difficulty: Easy                   """

n = int(input())
items = input().split()
sum = 0
for i in range(n):
    sum += int(items[i])
average = (sum / n)
print(f"{average:10.12f}")

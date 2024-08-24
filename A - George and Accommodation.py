"""              Author: Mohammed Sadik
                 Language: Python 3
                 Difficulty: Easy                """

n = int(input())
for i in range(n):
  count = 0
  num, room = map(int, input().split())
  if room - num >= 2:
    count += 1
print(count)

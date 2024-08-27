"""              Author: Mohammed Sadik
                 Language: Python 3
                 Difficulty: Easy                  """

n = int(input())
if n % 2 == 0:
    ans = int(n / 2)
else:
    ans = "-" + str((int(n / 2) + 1))
print(ans)

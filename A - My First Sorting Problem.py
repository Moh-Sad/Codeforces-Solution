"""              Author: Moahmmed Sadik
                 Language: Python 3
                 Difficulty: Easy               """

cases = int(input())
for _ in range(cases):
    x, y = map(int, input().split())
    print(str(min(x, y)) + " " + str(max(x, y)))

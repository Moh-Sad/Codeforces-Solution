"""              Author: Moahmmed Sadik
                 Language: Python 3
                 Difficulty: Easy(Tricky)               """

cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    print( n * k - (k - 1))

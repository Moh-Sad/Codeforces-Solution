"""             Author: Mohammed Sadik
                Language: Python 3
                Difficulty: Easy               """

from math import *
cases = int(input())
for i in range(cases):
    max = int(input())
    items = list( map(int, input().split()))
    total = sum(items)
    if int(sqrt(total)) * int(sqrt(total)) == total:
        print("YES")
    else:
        print("NO")

"""    Author: Mohammed Sadik
       Language: Python 3
       Difficulty: Medium    """

for _ in range(int(input())):
    n = int(input())
    a = list( map(int, input().split()))
    max = 0
    for i in range(n):
        if n == 1:
            max = a[0]
        elif i % 2 != 0:
            continue
        elif a[i] > max:
            max = a[i]
    print(max)           

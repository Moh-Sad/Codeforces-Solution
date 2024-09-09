"""             Author: Mohammed Sadik
                Language: Python 3
                Difficulty: Easy               """

cases = int(input())
for _ in range(cases):
    max = int(input())
    a = list( map(int, input().split()))
    b = list( map(int, input().split()))
    up = 0
    down = 0
    count = 0
    while down < max:
        if b[down] < a[up]:
            count += 1
            down += 1
        else:
            down += 1
            up += 1
    print(count)
    count = 0

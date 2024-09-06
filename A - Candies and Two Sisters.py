"""             Author: Mohammed Sadik
                Language: Python 3
                Difficulty: Easy               """

cases = int(input())
for i in range(cases):
    candy = int(input())
    if candy < 3:
        print(0)
    elif candy % 2 != 0:
        ans = int(candy / 2)
        print(ans)
    else:
        ans = int(candy / 2) - 1
        print(ans)

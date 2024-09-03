"""                Author: Mohammed Sadik
                   Language: Python 3
                   Difficulty: Easy                    """

num = int(input())
for i in range(num):
    x = int(input())
    if x == 2:
        print(2)
    elif x % 2 == 0:
        print(0)
    else:
        print((2 - x % 2))

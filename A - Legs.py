"""    Author: Mohammed Sadik
       Language: Python 3
       Difficulty: Easy    """

for _ in range(int(input())):
    legs = int(input())
    count = 0
    while legs != 0:
        if legs >= 4:
            count += 1
            legs -= 4
        elif legs >= 2:
            count += 1
            legs -= 2
    print(count)

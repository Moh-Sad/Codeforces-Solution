"""    Author: Mohammed Sadik
       Language: Python 3
       Difficulty: MEDIUM    """

for _ in range(int(input())):
    num = int(input())
    items = list(input())
    count = 0
    for i in range(num):
        if items[i] == "(":
            count += 3
        elif items[i] == ")":
            count += 1
    print(count)

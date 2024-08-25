"""              Author: Mohammed Sadik
                 Language: Python 3
                 Difficulty: Medium                """

n = int(input())
cube = 0
for i in range(n):
    num, goal = map(int, input().split())
    if num == goal:
        print("Yes")
    elif num % 2 == 0 and goal % 2 == 0 and num > goal:
        print("Yes")
    elif num % 2 != 0 and goal % 2 != 0 and num > goal:
        print("Yes")
    else:
        print("No")

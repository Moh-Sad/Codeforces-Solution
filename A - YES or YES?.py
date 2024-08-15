"""        Author: Mohammed Sadik
           Language: Python 3
           Difficulty: Easy          """

n = int(input())
list1 = []
front = 0
for i in range(n):
    list1.append(input().lower())
    if list1[i] == "yes":
        print("YES")
    else:
        print("NO")

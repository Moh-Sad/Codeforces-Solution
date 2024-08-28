"""              Author: Mohammed Sadik
                 Language: Python 3
                 Difficulty: Easy                """

n = int(input())
for i in range(n):
    num = int(input())
    items = list(input())
    sorted_items = sorted(items)
    if items == sorted_items:
        print("YES")
    else:
        print("NO")

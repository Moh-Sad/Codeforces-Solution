"""    Author: Mohammed Sadik
       Language: Python 3
       Difficulty: Easy    """

n = int(input())
for i in range(n):
    t = input().split(" ")
    _list = [ int (i) for i in t]
    if _list[0] + _list[1] >= 10:
        print("YES")
    elif _list[0] + _list[2] >= 10:
        print("YES")
    elif _list[1] + _list[2] >= 10:
        print("YES")
    else:
        print("NO")

"""    
Author: Mohammed Sadik
Language: Python 3
Difficulty: Easy    
"""

for _ in range(int(input())):
    a, b = map(str, input().split())

    if a[-1] == "S" and b[-1] != "S":
        print("<")
    elif a[-1] == "S" and b[-1] =="S":
        if len(a) > len(b):
            print("<")
        elif len(a) == len(b):
            print("=")
        else:
            print(">")

    if a[-1] == "M" and b[-1] == "L":
        print("<")
    elif a[-1] == "M" and b[-1] == "M":
        print("=")
    elif a[-1] == "M" and b[-1] == "S":
        print(">")

    if a[-1] == "L" and b[-1] != "L":
        print(">")
    elif a[-1] =="L" and b[-1] == "L":
        if len(a) > len(b):
            print(">")
        elif len(a) == len(b):
            print("=")
        else:
            print("<")
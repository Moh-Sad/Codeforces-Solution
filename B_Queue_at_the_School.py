"""    Author: Mohammed Sadik
       Language: Python 3
       Difficulty: Medium    """

n, t = map(int, input().split())
items = list(input())
check = False
while t > 0:
    if len(items) == 1:
        break
    else:
        for i in range(1, n):
            if items[i - 1] == "B" and items[i] =="G" and check == False:
                items[i - 1] = "G"
                items[i] = "B"
                check = True
            else:
                check = False
    check = False
    t -= 1
            
items = "".join(items)
print(items)
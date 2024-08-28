"""              Author: Mohammed Sadik
                 Language: Python 3
                 Diffculty: Medium              """

n = int(input())
check = n
items = []
if n == 1:
    print("I hate it")
    n = 0
elif n == 2:
    print("I hate that I love it")
    n = 0
while n > 1 and check % 2 != 0:
    if n % 2 != 0:
        items.append("I hate that")
    else:
        items.append("I love that")
    n -= 1
while n > 1 and check % 2 == 0:
    if n % 2 != 0:
        items.append("I love that")
    else:
        items.append("I hate that")
    n -= 1
if len(items) != 0:
    if check % 2 == 0:
        items.append("I love it")
        for i in range(len(items)):
            print(items[i], end = " ")
    else:
        items.append("I hate it")
        for i in range(len(items)):
            print(items[i], end = " ")

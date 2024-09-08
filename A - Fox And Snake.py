"""             Author: Mohammed Sadik
                Language: Python 3
                Difficulty: Easy               """

r, c = map(int, input().split())
head = "#"
tail = "."
check = True
for i in range(r):
    if i % 2 == 0:
        print(head * c)
    elif i % 2 != 0 and check == True:
        print(tail * (c - 1) + head)
        check = False
    else:
        print(head + tail * (c - 1))
        check = True

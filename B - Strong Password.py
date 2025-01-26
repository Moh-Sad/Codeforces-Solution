"""    Author: Mohammed Sadik
       Language: Python 3
       Difficulty: Medium    """

for _ in range(int(input())):
    items = list(input())
    check = False
    for i in range(1, len(items)):
        if items[i - 1] == items[i]:
            if items[i] == "a":
                items.insert(i, "b")
            else:
                items.insert(i, "a")
            check = True
            break
    if check == False:
        if items[0] == "a":
            items.insert(0, "b")
        else:
            items.insert(0, "a")
    items = "".join(items)
    print(items)

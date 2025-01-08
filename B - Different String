"""             Author: Mohammed Sadik
                Language: Python 3
                Difficulty: Medium               """

cases = int(input())
for _ in range(cases):
    items = list(input())
    check = True
    for i in range(1, len(items)):
        if items[i - 1] != items[i]:
            check = False
    for _ in range(cases):
        if check == False:
            if sorted(items) == items:
                print("YES")
                items.sort(reverse = True)
                items = "".join(items)
                print(items)
                break
            else:
                items = sorted(items)
                items = "".join(items)
                print("YES")
                print(items)
                break
        else:
            print("NO")
            break

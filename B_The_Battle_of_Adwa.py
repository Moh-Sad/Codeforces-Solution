for _ in range(int(input())):
    items = list(input())
    if len(items) > 10:
        print(items[0] + str(len(items) - 2) + items[-1])
    else:
        print("".join(items))

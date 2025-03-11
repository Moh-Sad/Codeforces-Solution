for _ in range(int(input())):
    bag = []
    n = int(input())
    for i in range(n):
        items = list(input())
        for j in range(4):
            if items[j] == "#":
                bag.append(j + 1)
    swap = bag[::-1]
    for i in range(len(swap)):
        print(swap[i], end=" ")
    print(" ")
"""              Author: Moahmmed Sadik
                 Language: Python 3
                 Difficulty: Medium                """

cases = int(input())
for _ in range(cases):
    max = int(input())
    items = input().split()
    new = items[ :: ]
    n = 0
    l = 0
    r = -1
    k = 0
    check = True
    while n < max:
        if check == True:
            items[k] = new[l]
            check = False
            l = l + 1
            k += 1
            n += 1
        elif check == False:
            items[k] = new[r]
            check = True
            r = r - 1
            k += 1
            n += 1
    items = " ".join(items)
    print(items)

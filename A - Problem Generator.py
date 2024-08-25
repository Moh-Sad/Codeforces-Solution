"""              Author: Moahmmed Sadik
                 Language: Python 3
                 Difficulty: Hard                """

n = int(input())
for i in range(n):
    num, max = map(int, input().split())
    items = list(input())
    test = "ABCDEFG"
    count = 0
    for i in test:
        if int(items.count(i)) >= max:
            continue
        elif int(items.count(i)) == 0:
            count += max
        elif int(items.count(i)) < max:
            count = count + (max - int(items.count(i)))
    print(count)
    count = 0

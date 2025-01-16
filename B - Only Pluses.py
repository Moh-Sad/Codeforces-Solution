"""        Author: Mohammed Sadik
           Language: Python 3
           Difficulty: Medium          """

for _ in range(int(input())):
    items = list( map(int, input().split()) )
    n = 0
    sum = 0
    while n < 5:
            if min(items) == items[0]:
                items[0] = items[0] + 1
                n += 1
            elif min(items) == items[1]:
                items[1] = items[1] + 1
                n += 1
            else:
                 items[2] = items[2] + 1
                 n += 1
    print( items[0] * items[1] * items[2])

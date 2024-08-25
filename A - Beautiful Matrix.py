"""              Author: Mohammed Sadik
                 Language: Python 3
                 Difficulty: Easy                """

items = []
for i in range(5):
    collect = input().split()
    items.append(collect[0])
    items.append(collect[1])
    items.append(collect[2])
    items.append(collect[3])
    items.append(collect[4])
if int(items[0]) or int(items[4]) or int(items[20]) or int(items[24]) == 1:
    print(4)
elif int(items[5]) or int(items[9]) or int(items[15]) or int(items[19]) == 1:
    print(3)
elif int(items[1]) or int(items[3]) or int(items[21]) or int(items[23]) == 1:
    print(3)
elif int(items[7]) or int(items[11]) or int(items[13]) or int(items[17]) == 1:
    print(1)
elif int(items[12]):
    print(0)
else:
    print(2)

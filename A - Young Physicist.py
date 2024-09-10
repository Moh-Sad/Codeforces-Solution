"""             Author: Mohammed Sadik
                Language: Python 3
                Difficulty: Easy               """

max = int(input())
x, y, z = 0, 0, 0
for _ in range(max):
    items = list( map(int, input().split()))
    if items[0] > 0:
        x += items[0]
    else:
        x -= abs(items[0])
    if items[1] > 0:
        y += items[1]
    else:
        y -= abs(items[1])
    if items[2] > 0:
        z += items[2]
    else:
        z -= abs(items[2])
if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")

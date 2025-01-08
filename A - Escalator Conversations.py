"""             Author: Mohammed Sadik
                Language: Python 3
                Difficulty: Easy               """

for _ in range(int(input())):
    n, m, k, h = map(int,input().split())
    items = list( map(int, input().split()))
    bag = []
    count = 0
    for i in range(1, m):
        bag.append(i * k)
    for j in range(n):
        if abs(h - items[j]) in bag:
            count += 1
    print(count)

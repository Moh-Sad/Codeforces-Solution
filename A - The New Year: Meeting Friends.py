"""             Author: Mohammed Sadik
                Language: Python 3
                Difficulty: Easy               """

items = list( map(int, input().split()) )
items = sorted(items)
count = 0
count += items[2] - items[1]
count += items[1] - items[0]
print(count)

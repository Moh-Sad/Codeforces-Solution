"""             Author: Mohammed Sadik
                Language: Python 3
                Difficulty: Easy               """

cases = int(input())
for _ in range(cases):
    items = list( input())
    count = 0
    for i in range(5):
        if items[i] == "A":
            count += 1
    if count >= 3:
        print("A")
    else:
        print("B")

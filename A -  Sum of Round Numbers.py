"""             Author: Mohammed Sadik
                Language: Python 3
                Difficulty: Easy               """

test_cases = int(input())
count = 0
for i in range(test_cases):
    num = list(input())
    care = len(num)
    items = []
    for j in range(len(num)):
        if int(num[j]) != 0:
            count += 1
            calculate = (num[j] + "0" * (care - 1))
            items.append(calculate)
        care -= 1
    items = ' '.join(items)
    print(count)
    print(items)
    count = 0

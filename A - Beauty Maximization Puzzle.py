"""              Author: Mohammed Sadik
                 Language: Python 3
                 Difficulty: Easy                """

num = int(input())
for i in range(num):
    sum = 0
    max = int(input())
    items = list( map(int, input().split()) )
    items = sorted(items)
    for j in range(1, max):
            sum = sum +  (items[j] - items[j - 1])
    print(sum)

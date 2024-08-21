"""            Author: Mohammed Sadik
               Language: Python 3
               Difficulty: Medium              """

cost, num, max = map(int, input().split())
items = []
count = 1
sum = 0
for i in range(max):
    items.append(cost * count)
    count += 1
for i in range(len(items)):
    sum += items[i]
if sum > num:
    print(sum - num)
else:
    print("0")

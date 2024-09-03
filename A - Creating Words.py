"""              Author: Mohammed Sadik
                 Language: Python 3
                 Difficulty: Easy                  """

num = int(input())
for i in range(num):
    items = list(input())
    swap = items[0]
    items[0] = items[4]
    items[4] = swap
    print(items[0]+items[1]+items[2]+" "+items[4]+items[5]+items[6])

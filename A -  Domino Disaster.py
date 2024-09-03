"""              Author: Mohammed Sadik
                 Language: Python 3
                 Difficulty: Easy                  """

num = int(input())
for j in range(num):
    max = int(input())
    items = list(input())
    for i in range(max):
        if  items[i] == "U":
            items[i] = "D"
        elif items[i] == "D":
            items[i] = "U"
    items = "".join(items)
    print(items)

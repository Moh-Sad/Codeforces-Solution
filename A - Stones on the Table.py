"""            Author: Mohammed Sadik
               Language: Python 3
               Difficulty: Easy            """

n = int(input())
items = list(input())
count = 0 
for i in range(n-1, 0, -1):
    if items[i] == items[i-1]:
            count += 1
print(count)

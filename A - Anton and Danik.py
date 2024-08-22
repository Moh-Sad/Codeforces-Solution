"""            Author: Mohammed Sadik
               Language: Python 3
               Difficulty: Easy                """"

num = int(input())
items = list(input())
count = 0
for i in range(num):
    if items[i] == "A":
        count += 1
if count > (num / 2):
    print("Anton")
elif count < (num / 2):
    print("Danik")
else:
    print("Friendship")

"""              Author: Mohammed Sadik
                 Language: Python 3
                 Difficulty: Easy                """

num = int(input())
check = "codeforces"
count = 0
for i in range(num):
    items = list(input())
    if items[0] != check[0]:
        count += 1
    if items[1] != check[1]:
        count += 1
    if items[2] != check[2]:
        count += 1
    if items[3] != check[3]:
        count += 1
    if items[4] != check[4]:
        count += 1
    if items[5] != check[5]:
        count += 1
    if items[6] != check[6]:
        count += 1
    if items[7] != check[7]:
        count += 1
    if items[8] != check[8]:
        count += 1
    if items[9] != check[9]:
        count += 1
    print(count)
    count = 0

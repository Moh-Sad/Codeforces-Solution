"""             Author: Mohammed Sadik
                Language: Python 3
                Difficulty: Medium               """

guest = input()
host = input()
guest_and_host = guest + host
items = input()
check = True
count_1 = []
count_2 = []
for i in range(len(items)):
    count_1.append(items.count(items[i]))
for i in range(len(guest_and_host)):
    count_2.append(items.count(guest_and_host[i]))
for i in range(len(items)):
    if items[i] not in guest_and_host:
        check = False
    elif (len(guest) + len(host)) != len(items):
        check = False
    elif sorted(count_1) != sorted(count_2):
        check = False
if check == True:
    print("YES")
else:
    print("NO")

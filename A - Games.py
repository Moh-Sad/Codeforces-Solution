"""             Author: Mohammed Sadik
                Language: Python 3
                Difficulty: Easy               """

n = int(input())
count = 0
host = []
guest = []
for i in range(n):
    x , y = map(int, input().split())
    host.append(x)
    guest.append(y)
for i in range(n):
    count = count + guest.count(host[i])
print(count)

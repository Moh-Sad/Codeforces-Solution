"""         Author: Mohammed Sadik 
            Language: Python 3
            Difficulty: Medium        """

max = int(input())
items = list( map(int,input().split()) ) 
count = 0
maxx = items[0]
minn = items[0]
for i in range(max):
    if items[i] > maxx:
        maxx = items[i]
        count += 1
    elif items[i] < minn:
        minn = items[i]
        count += 1
print(count)

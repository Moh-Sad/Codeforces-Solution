"""        Author: Mohammed Sadik
           Language: Python 3
           Difficulty: Hard        """

for _ in range(int(input())):
    n, k = map(int, input().split())
    items = list( map(int, input().split()) )
    items.sort()
    sum = 0
    for i in range(k - 1):
        if items[i] == 1:
            sum += 1
        else:
            sum = sum + (items[i] * 2) - 1 
    print(sum)

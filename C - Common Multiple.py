"""        Author: Mohammed Sadik
           Language: Python 3
           Difficulty: Medium       """

for _ in range(int(input)):
    n = int(input())
    items = list(map(int, input().split()))
    print(len(set(items)))
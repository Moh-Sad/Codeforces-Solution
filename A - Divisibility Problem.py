"""              Author: Mohammed Sadik
                 Language: Python 3
                 Difficulty: Easy                  """

n = int(input())
for i in range(n):
    num, max = map(int, input().split())
    if num % max == 0:
        Answer = 0
    else:
        Answer = max - (num % max)    
    print(Answer)

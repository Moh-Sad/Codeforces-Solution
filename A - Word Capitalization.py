""""          Author: Mohammed Sadik
             Language: Python 3
             Difficulty: Easy            """"

word = list(input())
fword = word[0].upper()
word[0] = fword
for i in range(len(word)):
    print(word[i], end ="")

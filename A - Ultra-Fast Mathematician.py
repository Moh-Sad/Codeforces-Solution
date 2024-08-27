"""              Author: Mohammed Sadik
                 Language: Python 3
                 Difficulty: Medium                """

group1 = list(input())
group2 = list(input())
ans = []
for i in range(len(group1)):
    if int(group1[i]) == int(group2[i]):
        ans.append(0)
    else:
        ans.append(1)
for i in range(len(ans)):
    print(ans[i], end = "")

"""             Author: Mohammed Sadik
                Language: Python 3
                Difficulty: Easy               """

n = int(input())
sum = 0
for i in range(n):
    polygon = input().lower()
    if polygon == "tetrahedron":
       sum += 4
    elif polygon == "cube":
       sum += 6
    elif polygon == "octahedron":
       sum += 8
    elif polygon == "dodecahedron":
       sum += 12
    else:
       sum += 20
print(sum)

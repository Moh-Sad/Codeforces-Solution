for _ in range(int(input())):
    n, k, p = map(int, input().split())
    if abs(n * p) >= abs(k):
        if int(abs(k/p)) == abs(k/p):
            print(int(abs(k/p)))
        else:
            print(int(abs(k/p)) + 1)
    else:
        print(-1)
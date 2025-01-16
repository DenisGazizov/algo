def func(a, b, rover):
    queue = [[], [], [], [], []]
    c, d = (i for i in range(1, 5) if i != a and i != b)
    ind = 0
    res = []
    for i in range(1, len(rover)):
        while ind < len(rover) and rover[ind][-1] == i:
            queue[rover[ind][0]].append(1)
            ind += 1

    return res


n = int(input())
a, b = map(int, input().split())
rover = [tuple(map(int, input().split())) for _ in range(n)]
rover.sort(key=lambda x: x[-1])
print(func(a, b, rover))
def func(database, queries):
    counter = 0
    for word in database:
        j = 0
        counter += 1
        while j < max(len(queries), len(word)):
            if j >= len(word):
                break
            if j >= len(queries):
                break
            if word[j] != queries[j]:
                break
            counter += 1
            j += 1
        else:
            break
    return counter

database = []
queries = []
N = int(input())
for _ in range(N):
    database.append(input())
Q = int(input())
for _ in range(Q):
    print(func(database, input()))





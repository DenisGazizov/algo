def football_stats(N, M, matches):
    arkady_diff = 0
    results = []
    for match in matches:
        gA, gB = match[0]
        players = match[1]
        if gA > gB:
            diffA, diffB = gA - gB, gB - gA
        elif gB > gA:
            diffA, diffB = gA - gB, gB - gA
        else:
            diffA = diffB = 0
        for i in range(5):
            if players[i] == 0:
                arkady_diff += diffA
            if players[i + 5] == 0:
                arkady_diff += diffB
        count = 0
        for i in range(5):
            if players[i] != 0:
                if gA > gB:
                    count += 1
                elif gA < gB:
                    count += 0
            if players[i + 5] != 0:
                if gA < gB:
                    count += 1
                elif gA > gB:
                    count += 0
        results.append(count)

    return results


N, M = map(int, input().split())
matches = []
for _ in range(M):
    gA, gB = map(int, input().split())
    players = list(map(int, input().split()))
    matches.append(((gA, gB), players))

result = football_stats(N, M, matches)

for res in result:
    print(res)


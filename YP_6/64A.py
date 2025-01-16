p_tree = {}
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent
heights = {}
for man in set(p_tree.keys()).union(set(p_tree.values())):
    if man in heights:
        continue
    temp_man = man
    c = 0
    while temp_man not in heights:
        if temp_man not in p_tree:
            heights[temp_man] = 0
            break
        else:
            c += 1
            temp_man = p_tree[temp_man]
    heights[man] = heights[temp_man] + c
for key, value in sorted(heights.items()):
    print(key, value)
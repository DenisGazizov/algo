def ancestor(child):
    a1 = [child]
    while child in p_tree:
        temp = p_tree[child]
        a1.append(temp)
        child = temp
    return a1

p_tree = {}
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent
ancestors = {}
while True:
    try:
        child1, child2 = input().split()
        if child1 not in ancestors:
            n = set(ancestor(child1))
            ancestors[child1] = n
        else:
            n = ancestors[child1]
        for anc in ancestor(child2):
            if anc in n:
                print(anc)
                break
    except:
        break
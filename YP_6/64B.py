def is_children(name, p_tree, potomok):
    if name not in p_tree:
        return 0
    elif name in potomok:
        return potomok[name]
    else:
        res = len(p_tree[name])
        for child in p_tree[name]:
            res += is_children(child, p_tree, potomok)
        return res

p_tree = {}
children = set()
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree.setdefault(parent, []).append(child)
    children.add(child)
    children.add(parent)
counter = 0
potomok = {}
for j in children:
    n = is_children(j, p_tree, potomok)
    potomok[j] = n

for key, value in sorted(potomok.items()):
    print(key, value)



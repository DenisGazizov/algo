class Tree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def add(root, data):
    if data == root.value:
        print('ALREADY')
        return
    if root.value is None:
        root.value = data
        root.left = Tree()
        root.right = Tree()
        print('DONE')
    elif data > root.value:
        add(root.right, data)
    else:
        add(root.left, data)


def search(root, data):
    if data == root.value:
        print('YES')
        return
    if not root.value:
        print('NO')
        return
    elif data < root.value:
        search(root.left, data)
    else:
        search(root.right, data)


def printtree(root, deep=0):
    if root.value is None:
        return
    printtree(root.left, deep+1)
    print(''.join(['.' * deep, str(root.value)]))
    printtree(root.right, deep+1)



root = Tree()

while True:
    try:
        command = input().split()
        if command[0] == 'PRINTTREE':
            printtree(root)
        elif command[0] == 'ADD':
            add(root, data=int(command[1]))
        elif command[0] == 'SEARCH':
            search(root, data=int(command[1]))
    except:
        break
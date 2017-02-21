def tree(root, branches=[]):
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, n=0):
    print (n * " " + str(root(t)))
    for b in branches(t):
        print_tree(b, n + 2)


def square_tree(t):
    if is_leaf(t):
        return tree(root(t) ** 2)
    else:
        return tree(root(t) ** 2, [square_tree(b) for b in branches(t)])

def height_tree(t):
    if is_leaf(t):
        return 0
    else:
        return 1 + max(height_tree(b) for b in branches(t))


def tree_max(t):
    if is_leaf(t):
        return root(t)
    else:
        max_val_branches = max(tree_max(b) for b in branches(t))
        return max(root(t), max_val_branches)


def in_tree(t, x):
    if is_leaf(t):
        return root(t) == x
    else:
        return any(in_tree(b, x) for b in branches(t))


def find_path(t, x):
    """Inefficient. Going through the tree twice."""
    if not in_tree(t, x):
        return None
    elif is_leaf(t) and root(t) == x:
        return [root(t)]
    else:
        path = [find_path(b, x) for b in branches(t) if in_tree(b, x)][0]
        return [root(t)] + path

def prune(t, k):
    if k == 0:
        return tree(root(t))
    else:
        sticks = [prune(b, k - 1) for b in branches(t)]
        return tree(root(t), sticks)


def hailstone_tree(n, h):
    if h == 0:
        return tree(n)
    else:
        right = hailstone_tree(n * 2, h - 1)
        if (n - 1) / 3 % 2 != 0 and (n - 1) % 3 == 0 and (n - 1) // 3 != 1:
            left = hailstone_tree((n - 1) // 3, h - 1)
            return tree(n, [right, left])
        else:
            return tree(n, [right])











        







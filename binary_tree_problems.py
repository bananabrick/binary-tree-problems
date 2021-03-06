# trees

# recursive description of trees (wooden trees)
# - a tree has a roor value and a list of branches
# - a tree with 0 branches is called a leaf

# relative description of trees (family trees)
# - nodes with values
# - each node is the root value of some other tree
# - each parent node is the sum of all child nodes

# implementing a tree using the recurisve definition
# each tree consists of a root and a list of branches
# alright, let's get started
# I'll implement a binary tree using the definition in the README

def binary_tree(root, branches=[]):
    for branch in branches:
        assert is_binary_tree(branch)
    return [root] + branches

def is_binary_tree(t):
    if type(t) != list or len(t) < 1 or len(branches(t)) > 2:
        return False
    else:
        for branch in branches(t):
            if not is_binary_tree(branch):
                return False
        return True

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        return sum(count_leaves(b) for b in branches(tree))

def sum_leaves(tree):
    if is_leaf(tree):
        return root(tree)
    else:
        return sum(sum_leaves(b) for b in branches(b))

def list_leaves(tree):
    if is_leaf(tree):
        return tree
    else:
        return sum([list_leaves(b) for b in branches(tree)], [])

def increment_leaves(t):
    if is_leaf(t):
        return tree(root(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(root(t), bs)

def increment(t):
    """Return a tree like t but with all node values incremented."""
    r = root(t) + 1
    bs = [increment(b) for b in branches(t)]

    return tree(r, bs)

def print_tree(t, indent=0):
    print ('  ' * indent + str(root(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        return sum(count_leaves(b) for b in branches(t))


def sum_leaves(t):
    if is_leaf(t):
        return root(t)
    else:
        return sum(sum_leaves(b) for b in branches(t))


def list_leaves(t):
    if is_leaf(t):
        return [root(t)]
    else:
        return sum([list_leaves(b) for b in branches(t)], [])

def increment_leaves(t):
    if is_leaf(t):
        return binary_tree(root(t) + 1)
    else:
        return binary_tree(root(t), [increment_leaves(b) for b in branches(t)])

def increment(t):
    root = root(t) + 1
    return binary_tree(root, [increment(b) for b in branches(t)]) 

def count_nodes(t):
    if not branches(t):
        return 1
    else:
        return 1 + sum(count_nodes(b) for b in branches(t))

def fib_binary_tree(n):
    if n < 1:
        return binary_tree(1)
    else:
        left, right = fib_binary_tree(n - 1), fib_binary_tree(n - 2)
        return binary_tree(root(left) + root(right), [left, right])

def max_depth(t):
    if is_leaf(t):
        return 0
    else:        
        return 1 + max(max_depth(b) for b in branches(t))

def min_value(t):
    if is_leaf(t):
        return root(t)
    else:
        min_in_branches = min(min_value(b) for b in branches(t))
        return min(min_in_branches, root(t))

def post_order(t):
    if is_leaf(t):
        print (root(t))
    else:
        for b in branches(t):
            post_order(b)
        print (root(t))
        
def has_path_sum(t, s):
    if is_leaf(t):
        return root(t) == s
    else:
        has_sum = [has_path_sum(b, s - root(t)) for b in branches(t)]
        return any(has_sum)

    
def same_tree(t1, t2):
    if is_leaf(t1) and is_leaf(t2):
        return root(t1) == root(t2)
    elif is_leaf(t1) and not is_leaf(t2):
        return False
    else:
        branches_t1 = branches(t1)
        branches_t2 = branches(t2)
        if len(branches_t1) != len(branches_t2):
            return False
        confirm_same_branches = all(same_tree(b1, b2) 
                                    for b1, b2 in zip(branches_t1, 
                                                      branches_t2))
        return root(t1) == root(t2) and confirm_same_branches

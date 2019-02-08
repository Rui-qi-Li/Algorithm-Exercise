from BST import *
# find height of tree
def height(root):
    if not root:
        return 0
    return max(height(root.left),height(root.right))+1

# check if a BST is balanced
def isBalanced(root):
    # base case
    if not root:
        return True # empty tree is balanced
    lh = height(root.left)
    rh = height(root.right)

    if abs(lh-rh) <= 1 and isBalanced(root.left) and isBalanced(root.right):
        return True
    return False

# optimized version
def isBalanced2(root):
    if isBalancedOpt == -1:
        return False
    else:
        return True

# isBalanced helper
def isBalancedOpt(root): # avoid calling height function over and over again
    if not root:
        return 0
    # if left subtree is unbalanced, the original tree is unbalanced
    lh = isBalancedOpt(root.left)
    if lh == -1:
        return -1
    rh = isBalancedOpt(root.right)
    if rh == -1:
        return -1

    if abs(lh-rh) > 1:
        return -1 # return to higher lh/rh calling function
    # else this tree is balanced, return its height
    return max(lh,rh) + 1

# convert a BST to AVL
def convertToAVL(tree):
    alist = inorderList(tree.root)
    tree.root = sortedToAVL(alist)
    return tree

# helper funciton, return BST print to a list
def inorderList(root):
    # base case
    if not root:
        return []

    leftT = inorderList(root.left)
    rightT = inorderList(root.right) # print right
    return leftT + [root.data] + rightT # corresponding to each recursive call

# helper function, convert a sorted list to AVL
def sortedToAVL(alist):
    # base case
    if not len(alist):
        return None

    mid = len(alist)//2
    root = Node(alist[mid])

    treel = alist[0:mid]
    treer = alist[mid+1:]

    root.left = sortedToAVL(treel)
    root.right = sortedToAVL(treer)
    return root # return to the higher level function

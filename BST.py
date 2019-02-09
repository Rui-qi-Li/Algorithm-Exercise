class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def getChildren(self):
        children=[]
        if self.left:
            children.append(self.left)
        if self.right:
            children.append(self.right)
        return children


class BST:
    def __init__(self,data):
        self.root = Node(data)
    def insert(self,data):
        if not self.root:
            self.root =Node(data)
        else:
            self.insertNode(self.root,data)
    def insertNode(self,curr,data):
        if data<=curr.data:
            if curr.left:
                self.insertNode(curr.left,data)
            else:
                curr.left = Node(data)
        else:
            if curr.right:
                self.insertNode(curr.right,data)
            else:
                curr.right = Node(data)
    def find(self,data):
        return self.findNode(self.root,data)
    def findNode(self,curr,data):
        if not curr:
            return False
        elif data == curr.data:
            return True
        elif data < curr.data:
            return self.findNode(curr.left,data)
        elif data > curr.data:
            return self.findNode(curr.right,data)
    def inorder(self):
        if not self.root:
            return 'Empty tree'
        else:
            self.inorderNode(self.root)

    def inorderNode(self,curr):
        if curr.left: # print left
            self.inorderNode(curr.left)
        print(curr.data) # print root
        if curr.right:
            self.inorderNode(curr.right) # print right
    def preorder(self):
        if not self.root:
            return 'Empty tree'
        else:
            self.preorderNode(self.root)
    def preorderNode(self,curr):
        if not curr:
            return
        print(curr.data) # print root
        self.preorderNode(curr.left) # print left
        self.preorderNode(curr.right) #print right

    def minvalue(self):
        if not self.root:
            return 'Empty tree'
        else:
            minNode = self.minvalueNode(self.root)
            print(minNode.data)
    def minvalueNode(self,curr):
        while curr.left:
            curr = curr.left
        return curr
    def delete(self,data):
        if not self.root:
            return 'Empty tree, del reject'
        else:
            self.deleteNode(self.root,data)
    def deleteNode(self,curr,data):
        # base case
        if not curr:
            return curr # None
        if data < curr.data:
            curr.left = self.deleteNode(curr.left,data)
        elif data > curr.data:
            curr.right = self.deleteNode(curr.right,data)
        else: # found node need to be deleted
            # 0/1 right child
            if not curr.left:
                temp = curr.right
                curr = None
                return temp
            elif not curr.left:
                temp = curr.left
                curr = None
                return temp
            # 2 children
            # get the inorder successor (smallest in the right subtree)
            temp = self.minvalueNode(curr.right)
            # copy the inorder successor's content to this Node
            curr.data = temp.data
            # delete the inorder successor, single leaf
            self.deleteNode(curr.right, temp.data)
        return curr # return curr/curr.left/curr.right

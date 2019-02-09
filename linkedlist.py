class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def printL(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def remove(self,data):
        prev = None
        curr = self.head
        while curr:
            if curr.data == data: # found the removed node
                if prev: # removed node is not the head
                    prev.next = curr.next
                else: # head is removed node
                    self.head = curr.next
            else: # keep tracking
                prev = curr # save curr states
                curr = curr.next
        return False # emply list or not found
        

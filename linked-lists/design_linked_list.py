

## Best practice solution

class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def addAtHead(self, val):
        newNode = Node(val)
        nextNode, prevNode = self.head.next, self.head

        newNode.next = nextNode
        newNode.prev = prevNode

        prevNode.next = newNode
        nextNode.prev = newNode

    def addAtTail(self, val):
        newNode = Node(val)
        nextNode, prevNode = self.tail, self.tail.prev

        newNode.next = nextNode
        newNode.prev = prevNode

        nextNode.prev = newNode
        prevNode.next = newNode

    def get(self, index):
        if not self.head or index < 0:
            return -1

        cur = self.head.next
        while index > 0 and cur != self.tail:
            cur = cur.next
            index -= 1

        if cur == self.tail or not cur:
            return -1

        return cur.val

    def addAtIndex(self, val, index):
        newNode = Node(val)
        cur = self.head.next

        while index > 0 and cur:
            cur = cur.next
            index -= 1

        if index < 0 or not cur:
            print(f"Invalid index was provided")
            return


        prevNode, nextNode = cur.prev, cur
        newNode.next = nextNode
        newNode.prev = prevNode

        prevNode.next = newNode
        nextNode.prev = newNode

    def deleteAtIndex(self, index):
        if index < 0:
            print("Invalid index was provided")
            return
        if not self.head.next:
            print("List is empty")
            return

        cur = self.head.next
        while index > 0 and cur:
            cur = cur.next
            index -= 1

        if not cur or cur == self.tail:
            print("Invalid Index was provided")
            return

        prev, next = cur.prev, cur.next
        prev.next = next
        next.prev = prev
        



    def __str__(self):
        lnkdList = ''
        lnkdListRv = ''
        node = self.head
        while node:
            lnkdList += str(node.val)
            if node.next:
                lnkdList += ' -> '
            if node.prev:
                lnkdListRv += ' <- '
            lnkdListRv += str(node.val)
            node = node.next


        return f'{lnkdList} \n{lnkdListRv}' 
                



linkedList = LinkedList()
linkedList.addAtHead(1)
linkedList.addAtTail(2)
linkedList.deleteAtIndex(-1)
print(linkedList)



## My first solution : 

# class Node:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

# class MyLinkedList:

#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def get(self, index: int) -> int:
#         node = self.head

#         if index < 0 or not node:
#             return -1

#         while index > 0:
#             node = node.next
#             index -= 1

#             if not node:
#                 return -1
        
#         return node.val

        
#     def addAtHead(self, val: int) -> None:
#         if not self.head:
#             self.head = Node(val)
#             self.tail = self.head
#         else:
#             newNode = Node(val, self.head, None)
#             self.head.prev = newNode
#             self.head = newNode

#     def addAtTail(self, val: int) -> None:
#         if not self.tail:
#             self.addAtHead(val)
#         else:
#             newNode = Node(val, None, self.tail)
#             self.tail.next = newNode
#             self.tail = newNode

#     def addAtIndex(self, index: int, val: int) -> None:
#         node = self.head

#         if index == 0:
#             self.addAtHead(val)
#             return
        
#         while index > 0 and node:
#             node = node.next
#             index -= 1
        
#         if index == 0 and not node:
#             self.addAtTail(val)
#             return
        
#         if index > 0 and not node:
#             return
        
#         newNode = Node(val, node, node.prev)
#         node.prev.next = newNode
#         node.prev = newNode

#     def deleteAtIndex(self, index: int) -> None:
#         node = self.head

#         if not node:
#             return

#         if index == 0:
#             if not node.next:
#                 self.head = None
#                 self.tail = None
#                 return 
                
#             node = node.next
#             node.prev = None
#             self.head = node
#             return
        
#         while index > 0 and node:
#             node = node.next
#             index -= 1
        
#         if not node:
#             return
        
#         if not node.next:
#             node.prev.next = None
#             self.tail = node.prev
#             return
        
#         node.prev.next = node.next
#         node.next.prev = node.prev
        
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
    def insert(self, val, index):
        cur = self.head.next
        while index > 0 and cur:
            index -= 1
            cur = cur.next
        if index == 0 and cur:
            new_node = ListNode(val)
            next_node, prev_node = cur, cur.prev

            prev_node.next = new_node
            next_node.prev = new_node
            new_node.prev = prev_node
            new_node.next = next_node
    
    def reverseList(self):
        cur = self.head.next

        while cur and cur != self.tail:
            next = cur.next
            prev = cur.prev

            cur.next = prev
            cur.prev = next
            cur = cur.prev
        
        self.tail.next,self.tail.prev = self.tail.prev, self.tail.next
        self.head.next, self.head.prev = self.head.prev, self.head.next

        self.head, self.tail = self.tail, self.head
        



    def printList(self):
        cur = self.head.next
        result = ''
        while cur:
            if cur != self.tail:
                result += f'{cur.val} -> '
            cur = cur.next
        print(result + 'None.')

        

example_list = LinkedList()
example_list.insert(1,0)
example_list.insert(2,1)
example_list.insert(5,2)
example_list.printList()
example_list.reverseList()
example_list.printList()
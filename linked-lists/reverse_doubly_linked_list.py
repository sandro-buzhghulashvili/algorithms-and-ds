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
    def printList(self):
        cur = self.head.next
        result = ''
        while cur:
            if cur != self.tail:
                result += f'{cur.val} -> '
            cur = cur.next
        print(result + 'None.')
    def reverseList(self):
        cur = self.head.next

        while cur and cur != self.tail:
            next_node = cur.next
            prev_node = cur.prev
            cur.next = prev_node
            cur.prev = next_node
            cur = cur.prev
        
        new_head_real = self.tail.prev 
        new_tail_real = self.head.next

        self.head.next = new_head_real
        new_head_real.prev = self.head

        self.tail.prev = new_tail_real
        new_tail_real.next = self.tail

        

example_list = LinkedList()
example_list.insert(1,0)
example_list.insert(2,1)
example_list.insert(5,2)
example_list.printList()
example_list.reverseList()
example_list.printList()
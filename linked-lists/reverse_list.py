from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedList = None
        currNode = head
        while currNode:
            nextNode = currNode.next
            currNode.next = reversedList
            reversedList = currNode
            currNode = nextNode
        return reversedList


# recursive approach - my version:
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head

    self.res = None

    def reverse(node: Optional[ListNode]):
        if not node.next:
            self.res = node
            return node

        reversedList = reverse(node.next)
        node.next = None
        reversedList.next = node

        return reversedList.next

    reverse(head)
    return self.res

## recursive approach - optimal version:
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        reversedList = self.reverseList(head.next)
        head.next.next = head
        head.next = None
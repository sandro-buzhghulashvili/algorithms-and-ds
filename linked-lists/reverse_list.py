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
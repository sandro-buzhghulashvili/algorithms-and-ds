from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head.next
        resList = ListNode()
        tail = resList
        mergedVal = 0
        
        while cur:
            if cur.val != 0:
                mergedVal += cur.val
            else:
                tail.next = ListNode(mergedVal)
                tail = tail.next
                mergedVal = 0
            cur = cur.next
        
        return resList.next
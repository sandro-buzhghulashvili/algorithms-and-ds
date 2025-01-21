from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        reversedGroups = ListNode()
        tail = reversedGroups
        index = 0
        cur = head

        while cur:
            temp = cur
            count = 0
            while temp and count < k:
                temp = temp.next
                count += 1

            if count == k:  
                tmp = None
                for i in range(k):
                    nextNode = head.next
                    head.next = tmp
                    tmp = head
                    head = nextNode

                tail.next = tmp
                while tail.next:
                    tail = tail.next

                cur = head
            else:
                tail.next = cur
                break

        return reversedGroups.next

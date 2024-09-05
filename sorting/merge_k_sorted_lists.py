from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        sortedList = lists[0]
        def mergeSortedLists(l1, l2):
            dumbNode = ListNode()
            tail = dumbNode

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            if l1:
                tail.next = l1
            if l2: 
                tail.next = l2
            
            return dumbNode.next

        for i in range(1, len(lists)):
            sortedList = mergeSortedLists(sortedList, lists[i])

        return sortedList
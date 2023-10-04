class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        StoredNodes = {}
        while head != None:
            if head in StoredNodes:
                return True
            StoredNodes[head] = True
            head = head.next
        return False

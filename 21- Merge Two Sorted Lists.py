class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        TempList = ListNode(0)
        ReturnList = TempList
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                ReturnList.next = list1
                list1 = list1.next
            else:
                ReturnList.next = list2
                list2 = list2.next
            ReturnList = ReturnList.next
        if list1 != None:
            ReturnList.next = list1
            list1 = list1.next
        if list2 != None:
            ReturnList.next = list2
            list2 = list2.next
        return TempList.next
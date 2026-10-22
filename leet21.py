
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(arr):
    """数组 -> 链表"""
    dummy = ListNode()
    cur = dummy
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next

def print_list(head):
    """打印链表"""
    res = []
    cur = head
    while cur:
        res.append(str(cur.val))
        cur = cur.next
    print(" -> ".join(res))
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if list1==None:
            return list2
        if list2==None:
            return list1
        dummy=ListNode()
        pre=dummy
        while list1 and list2:
            if list1.val<list2.val:
                pre.next=list1
                list1=list1.next
            else:
                pre.next=list2
                list2=list2.next
            pre=pre.next
        if list1:
            pre.next=list1
        else:
            pre.next=list2
        return dummy.next
if __name__ == "__main__":
    l1 = build_list([1,2,4])
    l2 = build_list([1,3,4])
    solution = Solution()
    merged_head = solution.mergeTwoLists(l1, l2)
    print_list(merged_head)
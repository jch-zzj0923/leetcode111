
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
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy=ListNode()
        dummy.next=head
        fast,slow=dummy,dummy
        for _ in range(n+1):
            fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next
if __name__ == "__main__":
    head=build_list([1,2,3,4,5])
    solution=Solution()
    modified_head = solution.removeNthFromEnd(head, 2)
    print_list(modified_head)

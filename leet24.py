
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
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy=ListNode()
        dummy.next=head
        cur=dummy
        while cur.next and cur.next.next:
            a=cur.next
            b=cur.next.next
            a.next=b.next
            b.next=a
            cur.next=b
            cur=a
        return dummy.next
if __name__ == "__main__":
    l=build_list([1,2,3,4])
    solution=Solution()
    swapped_head=solution.swapPairs(l)
    print_list(swapped_head)
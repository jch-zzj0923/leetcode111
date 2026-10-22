
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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head                          
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None
        left=self.sortList(head)
        right=self.sortList(mid)
        dummy=ListNode()
        p0=dummy
        while left and right:
            if left.val<right.val:
                p0.next=left
                left=left.next
            else:
                p0.next=right
                right=right.next
            p0=p0.next
        if left:
            p0.next=left
        if right:
            p0.next=right
        return dummy.next
if __name__ == "__main__":
    l = build_list([4,2,1,3])
    solution = Solution()
    sorted_head = solution.sortList(l)
    print_list(sorted_head)
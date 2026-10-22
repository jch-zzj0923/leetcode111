
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
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        n=0
        cur=head
        while cur:
            n+=1
            cur=cur.next
        dummy=ListNode()
        dummy.next=head
        p0=dummy
        pre=None
        cur=p0.next
        while n>=k:
            n-=k
            for _ in range(k):
                nxt=cur.next
                cur.next=pre
                pre=cur
                cur=nxt
            nxt=p0.next
            p0.next=pre
            nxt.next=cur
            p0=nxt
        return dummy.next
if __name__ == "__main__":
    head=build_list([1,2,3,4,5])
    k=2
    solution=Solution()
    new_head = solution.reverseKGroup(head, k)
    print_list(new_head)
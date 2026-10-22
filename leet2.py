
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
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy=ListNode()
        cur=dummy
        carry=0
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            total=v1+v2+carry
            carry=total//10
            digal=total%10
            cur.next=ListNode(digal)
            cur=cur.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next
if __name__ == "__main__":
    l1=build_list([2,4,3])
    l2=build_list([5,6,4])
    solution=Solution()
    result=solution.addTwoNumbers(l1,l2)
    print("Result:")
    print_list(result)

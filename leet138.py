
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
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hashmap=dict()
        cur=head
        while cur:
            hashmap[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            hashmap[cur].next=hashmap.get(cur.next)
            hashmap[cur].random=hashmap.get(cur.random)
            cur=cur.next
        return hashmap[head]     
if __name__ == "__main__":
    head=build_list([7,13,11,10,1])
    solution=Solution()
    copied_head=solution.copyRandomList(head)
    print_list(copied_head)

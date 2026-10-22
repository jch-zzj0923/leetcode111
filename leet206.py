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
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        pre=None
        cur=head
        while cur:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        return pre 
if __name__ == "__main__":
    head=build_list([1,2,3,4,5])
    solution=Solution()
    reversed_head = solution.reverseList(head)
    print_list(reversed_head)
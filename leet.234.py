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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast,slow=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        pre=None
        cur=slow
        while cur:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        p1=pre
        p2=head
        while p1:
            if p2.val != p1.val:
                return False
            p1=p1.next
            p2=p2.next
        return True
if __name__ == "__main__":
    head=build_list([1,2,2,1])
    solution=Solution()
    print(f"Is palindrome: {solution.isPalindrome(head)}")

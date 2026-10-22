# leetcode111
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

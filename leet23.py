
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
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if  not lists:
            return None
        def merge_two(list1,list2):
            dummy=ListNode()
            p=dummy
            while list1 and list2:
                if list1.val<list2.val:
                    p.next=list1
                    list1=list1.next
                else:
                    p.next=list2
                    list2=list2.next
                p=p.next
            if list1:
                p.next=list1
            if list2:
                p.next=list2
            return dummy.next
        def mer_divide(left,right):
            if left==right:
                return lists[left]
            mid=(left+right)//2
            l=mer_divide(left,mid)
            r=mer_divide(mid+1,right)      
            return merge_two(l,r)
        return mer_divide(0,len(lists)-1)
if __name__ == "__main__":
    l1 = build_list([1,4,5])
    l2 = build_list([1,3,4])
    l3 = build_list([2,6])
    lists = [l1, l2, l3]
    solution = Solution()
    merged_head = solution.mergeKLists(lists)
    print_list(merged_head)

            
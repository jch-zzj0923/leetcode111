# 链表节点定义
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 工具：数组转链表，方便测试
def build_list(arr):
    dummy = ListNode()
    cur = dummy
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next

# 工具：打印链表，看结果
def print_list(head):
    res = []
    cur = head
    while cur:
        res.append(str(cur.val))
        cur = cur.next
    print(" -> ".join(res))

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA=headA
        pB=headB
        while pA!=pB:
            pA=pA.next if pA else headB
            pB=pB.next if pB else headA
        return pA
if __name__ == "__main__":
    # 构建链表A: 4 -> 1 -> 8 -> 4 -> 5
    listA = build_list([4, 1, 8, 4, 5])
    # 构建链表B: 5 -> 0 -> 1 -> 8 -> 4 -> 5
    listB = build_list([5, 0, 1])
    
    # 创建交点节点
    intersection = ListNode(8)
    intersection.next = ListNode(4)
    intersection.next.next = ListNode(5)
    
    # 将链表A和链表B连接到交点
    listA.next.next = intersection
    listB.next.next = intersection
    
    # 打印链表A和链表B
    print("List A:")
    print_list(listA)
    print("List B:")
    print_list(listB)
    
    # 查找交点
    solution = Solution()
    result = solution.getIntersectionNode(listA, listB)
    
    # 打印结果
    if result:
        print(f"Intersection at node with value: {result.val}")
    else:
        print("No intersection.")
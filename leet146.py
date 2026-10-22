

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
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()  # key: node
        # 虚拟头尾哨兵节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0


    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)


    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # 删除链表中的一个节点
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # 删除尾节点（淘汰最久未使用），返回这个节点
    def remove_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 已存在：更新值，放到头部
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            # 新建节点
            new_node = DLinkedNode(key, value)
            self.cache[key] = new_node
            self.add_to_head(new_node)
            self.size += 1
            # 超过容量，淘汰末尾
            if self.size > self.capacity:
                del_node = self.remove_tail()
                del self.cache[del_node.key]
                self.size -= 1
if __name__ == "__main__":
    obj = LRUCache(2)
    obj.put(1,1)
    obj.put(2,2)
    print(obj.get(1))
    obj.put(3,3)
    print(obj.get(2))



 
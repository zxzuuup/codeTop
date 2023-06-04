class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 迭代解法
def reverseList(head):
    pre = None1
    cur = head
    while cur is not None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre


# 递归解法

def reverseList2(head):
    if head is None or head.next is None:
        return head
    next = head.next
    revNode = reverseList2(head.next)
    next.next = head
    head.next = None
    return revNode


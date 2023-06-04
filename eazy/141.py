def hasCycle(head):
    if not head or not head.Next:
        return False
    fast = head
    slow = head
    while fast and fast.Next:
        slow = slow.Next
        fast = fast.Next.Next
        if fast == slow:
            return True
    return False
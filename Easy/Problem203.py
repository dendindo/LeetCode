# Problem 203

prev = None
curr = head

while curr is not None:
    if curr.val == val:
        if prev is None:
            head = curr.next
            curr = head
        else:
            prev.next = curr.next
            curr = prev.next
    else:
        prev = curr
        curr = curr.next

return head
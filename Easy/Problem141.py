# Problem 141

def hasCycle(self, head: Optional[ListNode]) -> bool:
    seen = set()

    temp = True

    if head == None:
        return False
    else:
        while temp:

            if head.next == None:
                return False
            else:
                if head in seen:
                    temp = False
                    return True
                else:
                    seen.add(head)
                    head = head.next
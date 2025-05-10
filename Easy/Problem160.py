# Problem 160

objects = set()

tempA = True

while tempA:
    if headA.next == None:
        objects.add(headA)
        break
    else:
        objects.add(headA)
        headA = headA.next

tempB = True

while tempB:


    if headB in objects:
        return headB
    elif headB.next == None:
        if headB in objects:
            return headB
        else:
            return None
    else:
        headB = headB.next
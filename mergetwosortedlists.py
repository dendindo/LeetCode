# Problem 21

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # Stores a single digit (0-9)
        self.next = next    # Points to the next node


l3 = ListNode(4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

k3 = ListNode(4)
k2 = ListNode(3, k3)
k1 = ListNode(1, k2)


current = l1
current2 = k1


list1 = []
list2 = []

if current.val == None:
    list1 = []
else:
    while current:
        list1.append(current.val)
        current = current.next

if current2.val == None:
    list2 = []
else:
    while current2:
        list2.append(current2.val)
        current2 = current2.next

final = list1 + list2
final.sort()

print(final)

dummy = ListNode()
current = dummy

for num in final:
    current.next = ListNode(num)
    current = current.next






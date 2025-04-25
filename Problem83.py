# Problem 83

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head5 = ListNode(3)
head4 = ListNode(3, head5)
head3 = ListNode(2, head4)
head2 = ListNode(1, head3)
head1 = ListNode(1, head2)

current = head1
list = []
while current:
    list.append(current.val)
    current = current.next

list2 = []
for x in list:
    if x in list2:
        pass
    else:
        list2.append(x)


dummy = ListNode()
current = dummy

for num in list2:
    current.next = ListNode(num)
    current = current.next

print(dummy.next)
print(list2)


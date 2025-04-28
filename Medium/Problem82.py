# Problem 83

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# head5 = ListNode(3)
# head4 = ListNode(2, head5)
# head3 = ListNode(1, head4)
# head2 = ListNode(1, head3)
# head1 = ListNode(1, head2)

head = [-3,-1,-1,0,0,0,0,0,2]
dummyinit = ListNode()
current = dummyinit

for i in head:
    current.next = ListNode(i)
    current = current.next


current = dummyinit.next
list = []
while current:
    list.append(current.val)
    current = current.next

dict = {}

for x in list:
    if x in dict:       
        dict[x] += 1
    else:
        dict[x] = 1

final = []
for x in list:
    if dict[x] == 1:
        final.append(x)
    else:
        pass




dummy = ListNode()
current = dummy

for num in final:
    current.next = ListNode(num)
    current = current.next


print(final)


# Problem 2

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # Stores a single digit (0-9)
        self.next = next    # Points to the next node


l12 = ListNode(3)
l11 = ListNode(4, l12)
l1 = ListNode(2, l11)

l22 = ListNode(4)
l21 = ListNode(6, l22)
l2 = ListNode(5, l21)

number1 = ''
number2 = ''

current = l1
current2 = l2
while current:
    number2 += str(current2.val)
    number1 += str(current.val)
    current = current.next
    current2 = current2.next

number1 = number1[::-1]
number2 = number2[::-1]
total = int(number1) + int(number2)

list1 = list(str(total))
list1.reverse()

listfinal = [int(y) for y in list1]
print(listfinal)




dum = ListNode(0)
current = dum

for digit in listfinal:
    current.next = ListNode(digit)
    current = current.next

result = dum.next
print(result)
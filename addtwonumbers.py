# Problem 2

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = ''
        number2 = ''

        current = l1
        current2 = l2
        while current or current2:
            if current:
                number1 += str(current.val)
                current = current.next
            if current2:
                number2 += str(current2.val)
                current2 = current2.next


        number1 = number1[::-1]
        number2 = number2[::-1]
        total = int(number1) + int(number2)

        list1 = list(str(total))
        list1.reverse()

        listfinal = [int(y) for y in list1]
        
        dum = ListNode(0)
        current = dum

        for digit in listfinal:
            current.next = ListNode(digit)
            current = current.next

        result = dum.next
        return result
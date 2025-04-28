# Problem 67

a = "1010"
b = "1011"




decimal_a = int(a, 2)
decimal_b = int(b, 2)

dec_sum = decimal_a + decimal_b

binary_string = bin(dec_sum)

print(binary_string[2:])
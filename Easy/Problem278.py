# Problem 278

low = 0
high = 100
find = 3


while True:
    middle = (low + high) // 2
    print(f'Low: {low}')
    print(f'High: {high}')
    if find > middle:
        low = middle + 1
    
    elif find < middle:
        high = middle - 1

    elif find == middle:
        
        print(f'{find} was found.')
        break

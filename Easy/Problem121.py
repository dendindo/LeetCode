prices = [7,1,5,3,6,4]

if not prices:
    print(0)
else:
    min_price_so_far = prices[0]
    max_profit_so_far = 0

    for i in range(1, len(prices)):
        current_price = prices[i]
        potential_profit = current_price - min_price_so_far
        max_profit_so_far = max(max_profit_so_far, potential_profit)

        min_price_so_far = min(min_price_so_far, current_price)

    print(max_profit_so_far)

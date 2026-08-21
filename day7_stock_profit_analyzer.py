prices = [7, 1, 5, 3, 6, 4]

min_price = prices[0]
max_profit = 0

buy_day = 1
sell_day = 1

for i in range(1, len(prices)):

    if prices[i] < min_price:
        min_price = prices[i]
        buy_day = i + 1

    profit = prices[i] - min_price

    if profit > max_profit:
        max_profit = profit
        sell_day = i + 1

print("Stock Prices:", prices)
print("Maximum Profit:", max_profit)
print("Buy Day:", buy_day)
print("Sell Day:", sell_day)
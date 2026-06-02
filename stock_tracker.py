stock_prices = {
    "AAPL" : 180,
    "TSLA" : 250,
    "GOOG" : 150,
    "MSFT" : 300
}
print("Available Stocks: ")
for stock in stock_prices:
    print(stock)

    stock_name = input("\nEnter Stock Name: ").upper()
    quantity = int(input("Enter Quantity: "))

    if stock_name in stock_prices:
        total_investment = stock_prices[stock_name] * quantity

        print("\nStock:", stock_name)
        print("Price per Share:", stock_prices[stock_name])
        print("Quantity:", quantity)
        print("Total Investment Value:", total_investment)

        file = open("investment.txt", "w")
        file.write(f"Stock: {stock_name}\n")
        file.write(f"Price: {stock_prices[stock_name]}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Total Investment: {total_investment}\n")
        file.close()

        print("Result saved in investment.txt")

    else:
        print("Stock not found!")
prices = {
    "AAPL": 180,
    "TSLA": 250,
}

num_stocks = int(input("Enter the number of different stocks you own: "))

portfolio = {}
for i in range(num_stocks):
    symbol = input(f"Enter stock {i + 1} symbol: ").upper()
    qty = int(input(f"How many shares of {symbol}? "))
    portfolio[symbol] = portfolio.get(symbol, 0) + qty  # handles duplicates

grand_total = 0
details = []

print("\n----- Investment Summary -----")
for symbol, qty in portfolio.items():
    if symbol in prices:
        value = qty * prices[symbol]
        details.append((symbol, qty, prices[symbol], value))
        print(f"{symbol}: {qty} × {prices[symbol]} = {value}")
        grand_total += value
    else:
        print(f"{symbol}: Price not available!")

print(f"\n💰 Total Portfolio Value: {grand_total}")

choice = input("Do you want to save this report? (y/n): ").lower()
if choice == "y":
    fmt = input("Save as (txt/csv)? ").lower()

    if fmt == "txt":
        with open("portfolio_report.txt", "w") as f:
            f.write("----- Investment Report -----\n")
            for s, q, p, v in details:
                f.write(f"{s}: {q} × {p} = {v}\n")
            f.write(f"\nTotal = {grand_total}\n")
        print("✅ Report saved as portfolio_report.txt")

    elif fmt == "csv":
        import csv

        with open("portfolio_report.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            writer.writerows(details)
            writer.writerow(["Total", "", "", grand_total])
        print("✅ Report saved as portfolio_report.csv")

    else:
        print("⚠ Unknown format. Report not saved.")

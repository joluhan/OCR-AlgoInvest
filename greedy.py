import csv

def read_stock_data_from_csv(file_path):
    """Reads stock data from a CSV file and returns a list of tuples"""
    stocks = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        stock_reader = csv.reader(csvfile, delimiter=',')
        next(stock_reader)  # Skipping the header row
        for row in stock_reader:
            name = row[0]
            cost = float(row[1])
            profit_percentage = float(row[2].replace('%', ''))
            profit = cost * profit_percentage / 100
            stocks.append((name, cost, profit))
    return stocks

# Optimized investment algorithm using a greedy approach
def optimized_investment(stocks, max_investment=500):
    """Sorts and returns the best combination of stocks and the total profit"""
    # 
    sorted_stocks = sorted(stocks, key=lambda x: x[2]/x[1], reverse=True)

    total_cost = 0
    total_profit = 0
    selected_stocks = []

    for stock in sorted_stocks:
        if total_cost + stock[1] <= max_investment:
            selected_stocks.append(stock)
            total_cost += stock[1]
            total_profit += stock[2]

    return selected_stocks, total_profit
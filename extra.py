import csv

# Function to read stock data from a CSV file
def read_stock_data_from_csv(file_path):
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
    # Filtering out stocks with zero or negative costs or profits
    valid_stocks = [stock for stock in stocks if stock[1] > 0 and stock[2] >= 0]

    # Sorting stocks based on profit-to-cost ratio in descending order
    sorted_stocks = sorted(valid_stocks, key=lambda x: x[2]/x[1], reverse=True)

    total_cost = 0
    total_profit = 0
    selected_stocks = []

    for stock in sorted_stocks:
        if total_cost + stock[1] <= max_investment:
            selected_stocks.append(stock)
            total_cost += stock[1]
            total_profit += stock[2]

    return selected_stocks, total_profit

# File paths to the datasets
dataset1_path = 'Dataset/dataset1_Python+P7.csv'
dataset2_path = 'Dataset/dataset2_Python+P7.csv'

# Reading the datasets
dataset1 = read_stock_data_from_csv(dataset1_path)
dataset2 = read_stock_data_from_csv(dataset2_path)

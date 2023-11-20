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


# Brute force algorithm to find the best combination of stocks
def generate_combinations(stocks, max_investment=500):
    n = len(stocks)
    best_profit = 0
    best_combination = []

    # Recursive function to generate all combinations
    def generate_all_combinations(index=0, current_combination=[]):
        nonlocal best_profit, best_combination
        if index == n:
            total_cost = sum(stock[1] for stock in current_combination)
            total_profit = sum(stock[2] for stock in current_combination)
            if total_cost <= max_investment and total_profit > best_profit:
                best_profit = total_profit
                best_combination = current_combination.copy()
            return

        # Include current stock
        generate_all_combinations(index + 1, current_combination + [stocks[index]])

        # Exclude current stock
        generate_all_combinations(index + 1, current_combination)

    generate_all_combinations()
    return best_combination, best_profit

# File path to the CSV file
csv_file_path = 'Dataset/actions.csv'

# Reading the stock data and finding the best combination
stocks_from_csv = read_stock_data_from_csv(csv_file_path)
best_combination_csv, best_profit_csv = generate_combinations(stocks_from_csv)

# Printing the results
print("Best Stock Investment Combination:")
for stock in best_combination_csv:
    print(f"{stock[0]}: Cost {stock[1]} euros, Profit {stock[2]} euros")
print(f"Total Profit: {best_profit_csv:.2f} euros")
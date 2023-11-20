import csv
import time

start_time = time.time() # Start time of the algorithm

# Function to read stock data from a CSV file
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

# Applying the optimized investment algorithm to the datasets
best_combination_dataset1, best_profit_dataset1 = optimized_investment(dataset1)
best_combination_dataset2, best_profit_dataset2 = optimized_investment(dataset2)

# # Displaying the results
# print("Dataset 1 - Total Cost:", sum(stock[1] for stock in best_combination_dataset1), "Total Profit:", best_profit_dataset1)
# print("Dataset 2 - Total Cost:", sum(stock[1] for stock in best_combination_dataset2), "Total Profit:", best_profit_dataset2)

end_time = time.time() # End time of the algorithm

# Total execution time
execution_time = end_time - start_time 

# Function to print selected stock details with two decimal places
def print_selected_stocks(stocks, dataset_name):
    print(f"\nSelected Stocks for {dataset_name}:")
    for stock in stocks:
        print(f"{stock[0]}: Cost {stock[1]:.2f} euros, Profit {stock[2]:.2f} euros")
    total_cost = sum(stock[1] for stock in stocks)
    total_profit = sum(stock[2] for stock in stocks)
    print(f"Total Cost: {total_cost:.2f} euros, Total Profit: {total_profit:.2f} euros")

# Displaying the selected stocks for each dataset with formatted values
print_selected_stocks(best_combination_dataset1, "Dataset 1")
print_selected_stocks(best_combination_dataset2, "Dataset 2")
print(f"\nExecution Time: {execution_time:.2f} seconds")



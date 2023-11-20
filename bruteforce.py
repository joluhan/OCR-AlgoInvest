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
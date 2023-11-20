# Guide to Using Brute Force and Optimized Stock Investment Algorithms

**Introduction**

This guide provides step-by-step instructions on how to use two different algorithms for selecting stocks for investment: a brute force algorithm and an optimized algorithm. These methods are designed to help you find the most profitable combination of stocks within a set budget.

**Part 1: Using the Brute Force Algorithm**

    Data Preparation:
        Ensure you have a CSV file containing stock data. Each row should include the stock name, its cost, and profit percentage.

    Running the Brute Force Algorithm:
        Execute the brute force script. The script will read the stock data from your CSV file.
        The algorithm examines every possible combination of stocks to find the one that maximizes profit without exceeding your budget.

    Understanding the Output:
        The output will display the best combination of stocks and their total profit.
        Due to its exhaustive nature, this process can be time-consuming, especially with large datasets.

**Part 2: Using the Optimized Algorithm**

    Data Setup:
        Similar to the brute force method, have your stock data ready in a CSV file.

    Executing the Optimized Algorithm:
        Run the optimized investment script. This also starts by reading the stock data from the CSV file.
        The algorithm then sorts stocks by their profit-to-cost ratio and selects the most profitable stocks until the budget is reached or no more profitable stocks can be added.

    Interpreting the Results:
        The output will list the selected stocks, their cost, individual profit, and the total profit.
        This method is faster than the brute force approach and usually provides a near-optimal solution.

**Why Choose One Over the Other?**

    Brute Force Approach:
        Guarantees the best possible result.
        Better for smaller datasets due to its longer execution time.
    Optimized Approach:
        Provides a fast and efficient solution.
        Ideal for larger datasets where execution time is a concern.

**Conclusion**

Both methods offer unique advantages. The brute force algorithm ensures accuracy at the cost of time, while the optimized algorithm offers a balance between speed and precision. Choose the method that best suits your dataset size and time constraints.
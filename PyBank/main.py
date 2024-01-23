import os
import csv 

# This is my path 
# os.chdir(r'C:\Nafisa\Boot Camp\Module 3 Challenge\Starter_Code\PyBank')

total_months = 0
net_amount = 0
prev_month_value = None
monthly_changes = []
greatest_increase = ["", 0]  
greatest_decrease = ["", 0] 

# Define the path to the file within the Resources folder
file_path = 'Resources/budget_data.csv' 
# Open the CSV file
with open(file_path, mode='r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)
    # Skipping the header
    csv_header = next(file) 

    # Read each row in the file 
    for row in csv_reader:
        current_month_value = int(row[1])
        # Calculate the total months
        total_months += 1
        net_amount += current_month_value
        
        # Calculate the monthly change
        if prev_month_value is not None:
            change = current_month_value - prev_month_value
            monthly_changes.append(change)

            # Check for the greatest increase in profits
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]

            # Check for greatest decrease in profits
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]

        prev_month_value = current_month_value
        
    # Average change
    average_change = sum(monthly_changes) / len(monthly_changes)

# Print the financial results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Export the financial results to a text file
with open('analysis/financial_analysis.txt', 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_amount}\n")
    textfile.write(f"Average Change: ${average_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n") 
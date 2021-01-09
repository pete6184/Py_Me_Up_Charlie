# Import modules
import os
import csv

# Path to collect data from Resources Folder
bank_csv = os.path.join("Resources", "budget_data.csv")

# Specify the file to write to
# output_path = os.path.join("Analysis", "financial_analysis.txt")

# Assigning default values for variables
total_months = 0
total_change = 0
pnl_change_list = []
previous_value = 0
pnl_change= 0
greatest_increase = 0
greatest_decrease = 0
month_change = []

# Read in the CSV file
with open(bank_csv, "r") as csv_file:

    # Split the data on commas
    csvreader = csv.reader(csv_file, delimiter=",")

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

    # Define variable for total months
        total_months += 1

    # Define variable for total profit/loss
        total_change = total_change + int(row[1])
        
    # Define variable for average change 
        pnl_change = int(row[1]) - previous_value
        previous_value = int(row[1])
        pnl_change_list.append(pnl_change)
    
    # Find greatest month over month increase in profits
    for x in pnl_change_list:
        if x > greatest_increase:
            greatest_increase = x
    # index = pnl_change_list.index(greatest_increase)

    # Find greatest month over month decrease in profits 
    for y in pnl_change_list:
        if y < greatest_decrease:
            greatest_decrease = y
    # index = pnl_change_list.index(greatest_decrease)
      

# Print out our data

print("Financial Analysis")
print("------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_change}")
print(f"Average Change: ${round(sum(pnl_change_list)/(total_months),2)}")
print(f"Greatest Increase in Profits: ${greatest_increase}")
print(f"Greatest Decrease in Profits: ${greatest_decrease}")
# Import modules
import os
import csv

# Path to collect data from Resources Folder
bank_csv = os.path.join("Resources", "budget_data.csv")

# Assigning default values for variables
total_months = 0
total_change = 0
pnl_change_list = []
previous_value = 0
average_change= 0


# Read in the CSV file
with open(bank_csv, "r") as csv_file:

    # Split the data on commas
    csvreader = csv.reader(csv_file, delimiter=",")

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

    # Define variables
        total_months += 1
        total_change = total_change + int(row[1])
        average_change = int(row[1]) - previous_value
        previous_value = int(row[1])
        pnl_change_list.append(average_change)
        # greatest_increase =
        # greatest_decrease = 
      

        # Print out our data
print("Financial Analysis")
print("------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_change}")
print(f"Average Change: ${round(sum(pnl_change_list)/(total_months),2)}")
# print(f"Greatest Increase in Profits: {xxxx}")
# print(f"Greatest Decrease in Profits: {xxxxx}")
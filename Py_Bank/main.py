import os
import csv

# Path to collect data from Resources Folder
bank_csv = os.path.join("Resources", "budget_data.csv")

# Assign values for variables
date = int[0]
change = int[1]





# Read in the CSV file
with open(bank_csv, "r") as csv_file:

    # Split the data on commas
    csvreader = csv.reader(csv_file, delimiter=",")

    header = next(csvreader)

    # Loop through the data
    for row in csvreader
        
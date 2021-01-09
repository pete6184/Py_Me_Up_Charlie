# import modules
import os
import csv

# Path to collect data from Resources Folder
poll_csv = os.path.join("Resources", "election_data.csv")

# Specify the file to write to
# output_path = os.path.join("Analysis", "election_analysis.txt")

# Define default variables
total_votes = 0
vote_percentage = 0
candidate_votes = 0


# Read in the CSV file
with open(poll_csv, "r") as csv_file:

    # Split the data on commas
    csvreader = csv.reader(csv_file, delimiter=",")

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

#   The total number of votes cast
        total_votes += 1

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
# print(f"{candidate}, {vote_percentage}, {candidate_votes}")
# print(f"{candidate}, {vote_percentage}, {candidate_votes}")
# print(f"{candidate}, {vote_percentage}, {candidate_votes}")
# print(f"{candidate}, {vote_percentage}, {candidate_votes}")
print("----------------------------")
# print(f"{winner}")
print("----------------------------")



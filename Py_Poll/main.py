# import modules
import os
import csv

# Path to collect data from Resources Folder
poll_csv = os.path.join("Resources", "election_data.csv")

# Specify the file to write to
# output_path = os.path.join("Analysis", "election_analysis.txt")

# Define default variables
total_votes = 0
candidate_list = []
candidate_votes = {}
vote_percentage = {}


# Read in the CSV file
with open(poll_csv, "r") as csv_file:

    # Split the data on commas
    csvreader = csv.reader(csv_file, delimiter=",")

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

        # The total number of votes cast
        total_votes += 1

        # A complete list of candidates who received votes
        if str(row[2]) not in candidate_list:
            candidate_list.append(row[2])
        
        # The total number of votes each candidate won
        candidate_name = row[2]
        if not candidate_name in candidate_votes:
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# The percentage of votes each candidate won
for candidate, votes in candidate_votes.items():
    vote_percentage[candidate] = '{0:.0%}'.format(votes / total_votes)


# The winner of the election based on popular vote.


# Print out our statments
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {vote_percentage[candidate]} ({votes})")
print("----------------------------")

# print(f"Winner: {winner}")


# Export Data to text file
output_path = os.path.join("Analysis","election_analysis.txt")

with open(output_path, "w") as text:
    
    text.write(f"Election Results\n")
    text.write(f"----------------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write(f"----------------------------\n")
    for candidate, votes in candidate_votes.items():
        text.write(f"{candidate}: {vote_percentage[candidate]} ({votes})\n")
    text.write(f"----------------------------\n")
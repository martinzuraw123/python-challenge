# Print statement
print("Election Results")
print("-------------------------")

# Import the os module
import os
# Module for reading CSV files
import csv

# Set path for file
election_data = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('Analysis', 'poll_result.txt')

# Define variables
candidate_set = set()
candidate_votes = {}
total_votes = 0
winning_candidate = ""
most_votes = 0

# Reading using CSV module
with open(election_data) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvreader)
    # For Loop loop through the contents
    for row in csvreader:
        # Sum of the column as the loop goes down 1 row
        total_votes += 1
# Print statment of total votes as a string
print(f"Total votes: {total_votes}")
# Print statement
print("-------------------------")

# Reading using CSV module
with open(election_data) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvreader)
    # For Loop loop through the contents
    for row in csvreader:
        # Defining the variable as the the content in third column but position two
        candidate = row[2]
# Defining the variable as a list for the candidate set
candidate_list = list(candidate_set)

# Reading using CSV module
with open(election_data) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvreader)
    # For Loop loop through the contents
    for row in csvreader:
        # Defining the variable as the the content in third column but position two
        candidate = row[2]
        # Defining the variable using the list of the candidates as candidates vote using the get function in the first column position zero as in loops down the rows by one
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1
    # For Loop loop through the contents
    for candidate, votes in candidate_votes.items():
        # Calcutating the percentage varible by taking the number of votes each candidate got and dividing by total number of votes and then *100 to get the percent
        percentage = (votes / total_votes) * 100
        # Print statment of f-string of candidate name the precentage of vote received and number to votes received
        print(f"{candidate}: {percentage:.3f}% ({votes})")
        # Conditional statement if votes > most votes 
        if votes > most_votes:
            # And the most votes equals to the votes
            most_votes = votes
            # Then that makes the candidate the winner
            winning_candidate = candidate    
# Print statement
print("-------------------------")
# Print statment of f-string of the winning candidate
print(f"Winner: {winning_candidate}")
# Print statement
print("-------------------------")

# Open the file using "write" mode. Specify the variable to hold the contents in an output file
with open(output_path, 'w') as output_file:
    # Print statment for the output file in text format
    print("Election Results", file = output_file)
    # Print statment for the output file in text format
    print("-------------------------", file = output_file)
    # Print statment of f-string for the output file in text format
    print(f"Total votes: {total_votes}", file = output_file)
    # Print statment for the output file in text format
    print("-------------------------", file = output_file)
    # Print statment of f-string for the output file in text format
    # Needed to include the For Loop in order to print results for all three candidate not just one for the list
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})", file = output_file)
    # Print statement
    print("-------------------------", file = output_file)
    # Print statment of f-string for the output file in text format
    print(f"Winner: {winning_candidate}", file = output_file)
    # Print statment for the output file in text format
    print("-------------------------", file = output_file)
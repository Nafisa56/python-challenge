import os
import csv 

# This is my path
# os.chdir(r'C:\Nafisa\Boot Camp\Module 3 Challenge\Starter_Code\PyPoll') 


# Define the path to the file within the Resources folder
file_path = 'Resources/election_data.csv' 
vote_counts = {}
# Open the CSV file
with open(file_path, mode='r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)
    # Skipping the header
    csv_header = next(file)

    # Count votes
    total_votes = 0
    # Read each row in the file 
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]  
        if candidate not in vote_counts:
            vote_counts[candidate] = 1
        else:
            vote_counts[candidate] += 1

# Determine the winner            
winner = max(vote_counts, key=vote_counts.get)

# Print the election results

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in vote_counts.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the financial results to a text file
seperator = "-------------------------\n"
with open('analysis/election_results.txt', 'w') as textfile:
    textfile.write("Election Results\n")
    textfile.write(seperator)
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write(seperator)
    for candidate, votes in vote_counts.items():
        percentage = (votes / total_votes) * 100
        textfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    textfile.write(seperator)
    textfile.write(f"Winner: {winner}\n")
    textfile.write(seperator)
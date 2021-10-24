import os
import csv

csv_path = os.path.join('Resources', 'election_data.csv')

# Set Variables
voter_count = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0


with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Remove header
    csv_header = next(csv_reader)

    
    for row in csv_reader:
        #Count total Votes 
        voter_count += 1

    # Count Votes for each Candidate
        if row[2] == "Khan":
            Khan_votes += 1
        elif row[2] == "Correy":
            Correy_votes +=1    
        elif row[2] == "Li":
            Li_votes += 1
        else:
            OTooley_votes += 1

    #Look who won, with the possibility of a tie    
    if OTooley_votes > Correy_votes and OTooley_votes > Li_votes and OTooley_votes > Khan_votes:
        winner = "O'Tooley"
    elif Correy_votes > Li_votes and Correy_votes > Khan_votes and Correy_votes > OTooley_votes:
        winner = "Correy"
    elif Li_votes > Khan_votes and Li_votes > OTooley_votes and Li_votes > Correy_votes:
        winner = "Li"
    elif Khan_votes > OTooley_votes and Khan_votes > Correy_votes and Khan_votes > Li_votes:
        winner = "Khan"
    else:
        winner = "There is a tie"

    # Calculate percentages
    Khan_percentage = round((Khan_votes / voter_count) * 100, 2)
    Correy_percentage = round((Correy_votes / voter_count) * 100, 2)
    Li_percentage = round((Li_votes / voter_count) * 100, 2)
    OTooley_percentage = round((OTooley_votes / voter_count) * 100, 2)
    
    # create text file called poll_analysis
with open('analysis/poll_analysis.txt', 'w') as f:

    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {voter_count}\n")
    f.write("-------------------------\n")
    f.write(f"Khan: {Khan_percentage}% ({Khan_votes})\n")
    f.write(f"Correy: {Correy_percentage}% ({Correy_votes})\n")
    f.write(f"Li: {Li_percentage}% ({Li_votes})\n")
    f.write(f"O'Tooley: {OTooley_percentage}% ({OTooley_votes})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")


# Print Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {voter_count}")
print("-------------------------")
print(f"Khan: {Khan_percentage}% ({Khan_votes})")
print(f"Correy: {Correy_percentage}% ({Correy_votes})")
print(f"Li: {Li_percentage}% ({Li_votes})")
print(f"O'Tooley: {OTooley_percentage}% ({OTooley_votes})")
print("-------------------------")
print(f"Winner: {winner}")


# analysis_file = os.path.join("analysis/Poll_analysis.csv")
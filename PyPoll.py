#add dependencies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load= os.path.join("Resources","election_results.csv")
# Assign variable tosave file path
file_to_save= os.path.join("analysis", "election_analysis.txt")

#Initializeatotalvote counter
total_votes=0

#Candidate options and votes
candidate_options=[]
#declare dictionary
candidate_votes={}

winning_candidate=""
winning_count=0
winning_percentage=0

# Open election results and read the file
with open(file_to_load) as election_data:
    file_reader= csv.reader(election_data)

    #read the header row
    headers= next(file_reader)
#print each row in CSVfile
for row in file_reader:
    #add to thetotal vote count
    total_votes+=1
#print total votes  
    print (total_votes)
    #printcandidate name from Row
    candidate_name=row[2]
    #if the candidate does not match existing candidate
    if candidate_name not in candidate_options:
    #add candidate name to candidate list
        candidate_options.append(candidate_name)
#print(candidate_options)

        candidate_votes[candidate_name]=0
    candidate_votes[candidate_name]+=1
    with open(file_to_save,"w") as txt_file:
        # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
#print candidate vote dictionary
print (candidate_votes)

vote_percentage=(votes/total_votes)*100
#determine% ofvotes for ea candidate
#1 iterate thru list
for candidate_name in candidate_votes:
    votes= candidate_votes[candidate_name]
    vote_percentage= float(votes)/ float(total_votes)*100
    print(f"{candidate_name"}: received {vote_percentage} % of the vote.")

#determine if votes are greater than winning count
    If(votes> winning_count) and (vote_percentage>winning_percentage):
    # if tru then set winn_coount= votes and win_percent =
        winning_count=votes
        winning_percentage= vote_percentage
        winning_candidate= candidate_name
    candidate_results= (f"[candidate_name}: {vote_percentage:.1f]% ([votes:,])\n")
    print(candidate_results)
    txt_file.write(candidate_results)

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
txt_file.write(winning_candidate_summary)
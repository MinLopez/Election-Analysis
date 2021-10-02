import csv
import os
#Add file name variable that references path to file
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable for the file to load and the path.
#file_to_load='C:\Workspace\Election-Analysis\Resources\election_results.csv'


#Open Election File
with open(file_to_load) as election_data:
    #To do: Perform Analysis.
    print(election_data)
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote
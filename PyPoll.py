import csv
import os
#Add file name variable that references path to file
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Assign a variable for the file to load and the path.
# file_to_load='C:\Workspace\Election-Analysis\Resources\election_results.csv'


#Open Election File
with open(file_to_load) as election_data:
    #To do: Perform Analysis.
     # Read the file object with the reader function.
    file_reader = csv.reader(election_data) 
    # Print each row in the CSV file.
    for row in file_reader:
        print(row)


# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

   # Write three counties to the file.
     txt_file.write("Counties in the Election\n----------------------------\nArapahoe\nDenver\nJefferson")


# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote
# ---------------------------------------------------------------------------
#   Name of File: main.py
#   Discription: Creating a Python script for analyzing the financial records 
#                 You will give a set of financial data called budget_data.csv.
#   Import Modules: os, csv, collection
#   Input file: election_data.csv
#   Output file: ByPoll_analysis.txt
#   Created by: Minal Jajoo
#   -------------------------------------------------------------------------

# Import modules
import os
import csv

# Start of main program

# Give the path for the csv file
csvpath = os.path.join("Resources","election_data.csv")
# Give the path for the output-Result file
txtpath = os.path.join("Result","ByPoll_analysis.txt")

# Initialize all the variables 
TotalVotes = 0
candidateList =[]
WinnerVote = 0
EachResult =""

#Open the file and read 
with open (csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile,delimiter =',')
   
    # Skip the header
    next(csvreader,None)
    # Read and store the data from the 2nd row
    for row in csvreader:
        TotalVotes = TotalVotes + 1    #The total number of votes cast
        candidateList.append(row[2])  # List of candidates who received votes

    #The total number of votes each candidate won
    from collections import Counter
    candidate = Counter(candidateList)




for key,value in candidate.items():
    
    #The percentage of votes each candidate won
    VoteWon = format(value/TotalVotes *100,'.3f') 
    
    #The winner of the election based on popular vote
    if WinnerVote < value:   
        Winner = key 
        WinnerVote = value
    
    EachResult = EachResult + f"{key}: {VoteWon}% ({value})\n"
  # Final analysis:

   # print (key,": ",VoteWon,"% (",value,")",file = Export_file)
 
writeResult =(f''' 
--------------------------------- 
Election Results
---------------------------------   
Total Votes: {str(TotalVotes)} 
---------------------------------- 
{EachResult[:-1]}
---------------------------------
 Winner: {Winner}
---------------------------------''')

# final analysis: print to the terminal 
print (writeResult)

# export a text file with the results.
with open(txtpath,'w') as result:
        result.write(writeResult)
#-------------------------------------------------------------------------------------

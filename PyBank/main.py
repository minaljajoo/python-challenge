# ---------------------------------------------------------------------------
#   Name of File: main.py
#   Discription: Creating a Python script for analyzing the financial records 
#                You will give a set of financial data called budget_data.csv. 
#   Functions:  average
#   Import Modules: os, csv
#   Input file: budget_data.csv
#   Output file: ByBank_analysis.txt
#   Created by: Minal Jajoo
#   -------------------------------------------------------------------------

# Import modules
import os
import csv


# function - To calculate average 
def average(num):
    ave = float(sum(num)/len(num))
    return ave

#----------------------------------------------

# Start of main program

# Give the path for the csv file
csvpath = os.path.join("Resources","budget_data.csv")
# Give the path for the output-Result file
txtpath = os.path.join("Result","ByBank_analysis.txt")

# Initialize all the variables 
TotalMonth = 0
NetAmount = 0
MonthChange = []
change = 0.0
curValue = 0
AveChange = 0.0
GrtIncProfit = 0
GrtDecProfit = 0
#Open the file and read 
with open (csvpath,newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    
    # Skip the header
    next(csvreader,None)
    # Read and store the data from the 2nd row
    for row in csvreader:
        TotalMonth =  TotalMonth +1             #keep count of months
        NetAmount = NetAmount + int(row[1])     # The total net amount of "Profit/Losses" over the entire period
        
        change = (int(row[1]) - curValue)
        if curValue != 0:
            MonthChange.append(change)
           
            IncProfit = change
            DecProfit = change
        else:
            IncProfit = 0
            DecProfit = 0

#The greatest increase in profits (date and amount) over the entire period
        if IncProfit > GrtIncProfit:
            GrtIncProfit = IncProfit
            GrtIncMonth = row[0]

 #The greatest decrease in losses (date and amount) over the entire period           
        if DecProfit < GrtDecProfit:
            GrtDecProfit = DecProfit
            GrtDecMonth = row[0]
     
        curValue = int(row[1])
        
# Disply only 2 decimal places.
AveChange = round(average(MonthChange),2)


# Final analysis:
writeResult = (f"""
-----------------------------------------------------------
     Financial Analysis 
-----------------------------------------------------------
    Total Month: {str(TotalMonth)} 
    Total: ${str(NetAmount)} 
    Average Change: ${str(AveChange)}
    Greatest Increase in Profits : {GrtIncMonth}  (${str(GrtIncProfit)})
    Greatest Decrease in Profits : {GrtDecMonth}  (${str(GrtDecProfit)})
------------------------------------------------------------""")

# final analysis: print to the terminal 
print (writeResult)

# export a text file with the results.
with open(txtpath,'w') as result:
        result.write(writeResult)
#-------------------------------------------------------------------------------------
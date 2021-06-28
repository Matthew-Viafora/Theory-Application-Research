import csv
import os

path = os.path.dirname(os.path.abspath(__file__))

#Start by opening the affiliation CSV for a specific year (must manually change the filename)
with open(path+'/Affiliation_Parsing2010output.csv', "r") as AffiliationCSV: 
    affiliation_csv_reader = csv.reader(AffiliationCSV, delimiter=',')
    
    #Open the main CSV of one of the 5 conferences (must manually specify which conference)
    with open(path+'/NeurIPS-XML-output.csv', "r") as MainCSV:
        main_csv_reader = csv.reader(MainCSV, delimiter=',')
        
        #Parse through rows of both files
        for aRows in affiliation_csv_reader:
            print(aRows[5])                  #Error, works here but doesn't when placed within nested loop
            for mRows in main_csv_reader:
                
                #If the titles of each paper match, let the affiliations be updated for that paper
                if aRows[5] == mRows[7]:
                    print("Main file's first affilation before: " + mRows[3])
                    print("Main file's second affilation before: " + mRows[5])

                    #Update Affiliation data
                    mRows[3] = aRows[2]
                    mRows[5] = aRows[4]

                    print("Main file's first affilation after: " + mRows[3])
                    print("Main file's second affilation after: " + mRows[5])
# DESCRIPTION: This script is used for matching data from one CSV to another.
# Note: It may have to be modified to work with your CSV data.


import csv
import os
import pandas as pd

path = os.path.dirname(os.path.abspath(__file__))


affiliationCSV = pd.read_csv(path+'/ICML-affiliationsunique_affiliations.csv')
MainCSV = pd.read_csv(path+'/ICML-FINAL-COPY.csv')


        
count = 0
for index, row in MainCSV.iterrows():

    # try:

        count +=1
        print(count)
        for index_i, row_i in affiliationCSV.iterrows():
            if (row['first-author-affiliation'] == row_i['affiliation']):

                print("HIT")

                MainCSV['last-author-affiliation-country'][index] = affiliationCSV['country'][index_i]
                break
                


        
    # except:
    #     continue


MainCSV.to_csv(path+'NERUIPS-FINAL.csv')
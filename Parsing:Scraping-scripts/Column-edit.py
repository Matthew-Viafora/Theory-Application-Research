#DESCRIPTION: This script is used for editing a certain column of a certain CSV file

import csv
import os
import pandas as pd

path = os.path.dirname(os.path.abspath(__file__))

year = '2020'


affiliationCSV = pd.read_csv(path+'/NUERIPS-AFFILIATIONS.csv')

for i, row in affiliationCSV.iterrows():
    #put your edit at the end of this line of code below:
    affiliationCSV.at[i, 'title'] = affiliationCSV.at[i, 'title'].lower()
    



affiliationCSV.to_csv(path+'-'+year+'-affiliation'+'.csv')
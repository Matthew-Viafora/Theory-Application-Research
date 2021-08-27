# DESCRIPTION: THis file goes through affiliations and grabs the unique affiliation names and exports them into a CSV


from csv import DictReader
import os
import pandas as pd

path = os.path.dirname(os.path.abspath(__file__))
affiliation_csv_path1 = path+'/NuerIPS_affiliations_unique'

#edit path below
affiliation_csv_path = '/Users/mattviafora/Library/Mobile Documents/com~apple~CloudDocs/GitHub/Python Data Science/Theory-Application-Research/ICML affiliations/ICML-FINAL.csv'
print(affiliation_csv_path1)
print(affiliation_csv_path)

affiliation_csv = pd.read_csv(affiliation_csv_path)
rows = []
cols = ['affiliation']

for i in affiliation_csv['first-author-affiliation'].unique():
    rows.append({'affiliation': i})
for i in affiliation_csv['last-author-affiliation'].unique():
    rows.append({'affiliation': i})



df = pd.DataFrame(rows, columns=cols)
df_unique = pd.DataFrame(df['affiliation'].unique(), columns=cols)

df_unique.to_csv(path+"affiliation_final_list.csv")

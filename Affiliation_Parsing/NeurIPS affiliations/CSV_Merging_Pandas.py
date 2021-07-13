import pandas as pd
import os

path = os.path.dirname(os.path.abspath(__file__))

aDF = pd.read_csv(path + '/NeurIPS affiliations-2020-affiliation.csv')
mDF = pd.read_csv(path+'/T12020.csv')
count= 0

for aIndex, aRow in aDF.iterrows():
    count+=1
    print(count)
    
    for mIndex, row in mDF.iterrows():
        if ((aDF.iloc[aIndex,6]) == mDF.iloc[mIndex,7]):
            mDF.iloc[mIndex,3] = aDF.iloc[aIndex,3]
            mDF.iloc[mIndex,5] = aDF.iloc[aIndex,5]
            print(aDF.iloc[aIndex,6])
            break

mDF.to_csv(path+'/Final2020.csv')
import os
path = os.path.dirname(os.path.abspath(__file__))

#folders to iterate over
main_affiliation = "Affiliation_Parsing"
conference_affiliations = ["NeurIPS affiliations gender", "ICML affiliations gender"]

conference_lst = []

#returns list of conferences
def getConferenceList():
  #iterate over folders
    for main in conference_affiliations:
        gender_arr = os.listdir(path+'//Affiliation_Parsing'+'//'+main)
        conference_lst.append(gender_arr)
    return conference_lst

#returns partitioned string of conference i.e. NeurIPS-2010 => NeurIPS
def affiliationType(aff):
    conf = aff
    #partitions conference string
    partitioned_conf = conf.partition('-')
    return partitioned_conf[0]

data_lst = []

#returns list of paths to conference files i.e. ["Affiliation_Parsing\NeurIPS affiliations gender\NeurIPS-2010",...]
def getPathList():
    for conference_year in conference_lst:
        for conference in conference_year:
            data_lst.append("Affiliation_Parsing\\"+affiliationType(conference)+" affiliations gender\\"+conference)

def main():
    getConferenceList()
    getPathList()

    #example of getting files from one conference in the first folder
    print(os.listdir(path+"\\"+data_lst[0]))
  
main()
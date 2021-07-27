import os
path = os.path.dirname(os.path.abspath(__file__))

#folders to iterate over
main_affiliation = "Affiliation_Parsing"
conference_affiliations = ["NeurIPS affiliations gender", "ICML affiliations gender"]

conference_lst = []
#returns 
def getConferenceList():
  #iterate over folders
  for main in conference_affiliations:
    gender_arr = os.listdir(path+'//Affiliation_Parsing'+'//'+main)
    conference_lst.append(gender_arr)
  return conference_lst

def affiliationType(aff):
  x = aff
  y = x.partition('-')
  return y[0]+" affiliations gender"

data_lst = []
def getPathList():
  for conference_year in conference_lst:
    for conference in conference_year:
      data_lst.append("Affiliation_Parsing\\"+affiliationType(conference)+"\\"+conference)

def main():
  getConferenceList()
  getPathList()
  print(os.listdir(path+"\\"+data_lst[0]))
main()
import os
from posixpath import islink


class Iterate:   



    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))

        #folders to iterate over
        self.main_affiliation = "Affiliation_Parsing"
        self.conference_affiliations = ["NeurIPS affiliations gender", "ICML affiliations gender"]

        #initializes lists
        self.conference_lst = [] #list of conferences i.e. NeurIPS, ICML, etc.
        self.folder_lst = [] #list of paths of folders i.e. 'Affiliation_Parsing\\NeurIPS affiliations gender\\NeurIPS-2010', 'Affiliation_Parsing\\NeurIPS affiliations gender\\NeurIPS-2011', etc.
        self.csv_lst = [] #list of csv files (split into separate list by conference/year) i.e. [[NeurIPS2010xaa.csv,...], ['NeurIPS2011xaa.csv,...],...]
        self.combined_lst = [] #list of csv files combined i.e. [NeurIPS2010xaa.csv, NeurIPS2010xab.csv,...]
        self.path_lst = [] #list of pathways to csv files

    

    #returns list of conferences
    def get_conference_list(self):
    #iterate over folders
        for main in self.conference_affiliations:
            gender_arr = os.listdir(self.path+'//Affiliation_Parsing'+'//'+main)
            self.conference_lst.append(gender_arr)
        return self.conference_lst



    #returns partitioned string of conference i.e. NeurIPS-2010 => NeurIPS
    def affiliation_type(self, aff):
        conf = aff
        #partitions conference string
        partitioned_conf = conf.partition('-')
        return partitioned_conf[0]



    #returns list of paths to conference files i.e. ["Affiliation_Parsing\NeurIPS affiliations gender\NeurIPS-2010",...]
    def get_path_list(self):
        for conference_year in self.conference_lst:
            for conference in conference_year:
                self.folder_lst.append("Affiliation_Parsing\\"+self.affiliation_type(conference)+" affiliations gender\\"+conference)
        return self.folder_lst


    #returns list of csv files sorted by conference
    def get_csv_list(self):

        #gets conference and path list
        self.get_conference_list()
        self.get_path_list()

        counter = 0

        #iterates over 
        for i in self.folder_lst:
            self.csv_lst.append(os.listdir(self.path+"\\"+self.folder_lst[counter]))
            counter+=1
        return self.csv_lst

    #combined list of csv files from different conferences
    def combine_list(self):
        
        #gets csv list
        self.get_csv_list()

        #iterates over list of csv lists and appends them to a new array
        for csv_conf in self.csv_lst:
            for csv_file in csv_conf:
                self.combined_lst.append(csv_file)
        return self.combined_lst



    #returns path of year/conference from csv file input i.e. NeurIPS2010xaa.csv => NeurIPS-2010
    def affiliation_year(self, aff):
        conf = aff

        #partitions string to separate conference type from year
        partitioned_conf = conf.partition('x')
        partitioned_year = partitioned_conf[0].partition('2')

        return partitioned_year[0]+"-"+partitioned_year[1]+partitioned_year[2]



    #returns list of paths to access csv files from conferences
    def run(self):

        #gets combined csv list
        self.combine_list()
        counter = 0

        #iterates over combined csv list and appends path to each csv in a new array
        for i in self.combined_lst:
            self.path_lst.append(self.path+"\\Affiliation_Parsing\\"+self.affiliation_type(self.affiliation_year(self.combined_lst[counter]))+" affiliations gender\\"+self.affiliation_year(self.combined_lst[counter])+"\\"+self.combined_lst[counter])
            counter+=1

        return self.path_lst

#a = Iterate()
#print(a.run())
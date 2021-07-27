import os


class Iterate:   

    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))

        #folders to iterate over
        self.main_affiliation = "Affiliation_Parsing"
        self.conference_affiliations = ["NeurIPS affiliations gender", "ICML affiliations gender"]

        #initializes lists
        self.conference_lst = []
        self.data_lst = []

    #returns list of conferences
    def getConferenceList(self):
    #iterate over folders
        for main in self.conference_affiliations:
            gender_arr = os.listdir(self.path+'//Affiliation_Parsing'+'//'+main)
            self.conference_lst.append(gender_arr)
        return self.conference_lst

    #returns partitioned string of conference i.e. NeurIPS-2010 => NeurIPS
    def affiliationType(self, aff):
        conf = aff
        #partitions conference string
        partitioned_conf = conf.partition('-')
        return partitioned_conf[0]

    #returns list of paths to conference files i.e. ["Affiliation_Parsing\NeurIPS affiliations gender\NeurIPS-2010",...]
    def getPathList(self):
        for conference_year in self.conference_lst:
            for conference in conference_year:
                self.data_lst.append("Affiliation_Parsing\\"+self.affiliationType(conference)+" affiliations gender\\"+conference)

    #example of running program
    def run(self):
        self.getConferenceList()
        self.getPathList()
        print(os.listdir(self.path+"\\"+self.data_lst[0]))

a = Iterate()
print(a.run())
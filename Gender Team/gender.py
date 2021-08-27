
import os
from posixpath import islink

#imports pandas to read in data
import pandas as pd

#imports BS4 libraries for webscraping
from re import I
import requests
from bs4 import BeautifulSoup
#imports googlesearch to use requests and BS4 to scrape google
from googlesearch import search

class Gender():

    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))

        #folders to iterate over (only for folders with multiple years i.e. 2010, 2011, etc)
        self.main_affiliation = "Affiliation_Parsing"
        self.conference_affiliations = ["NeurIPS affiliations gender", "ICML affiliations gender"]

        #initializes lists
        self.conference_lst = [] #list of conferences i.e. NeurIPS, ICML, etc.
        self.folder_lst = [] #list of paths of folders i.e. 'Affiliation_Parsing\\NeurIPS affiliations gender\\NeurIPS-2010', 'Affiliation_Parsing\\NeurIPS affiliations gender\\NeurIPS-2011', etc.
        self.csv_lst = [] #list of csv files (split into separate list by conference/year) i.e. [[NeurIPS2010xaa.csv,...], ['NeurIPS2011xaa.csv,...],...]
        self.combined_lst = [] #list of csv files combined i.e. [NeurIPS2010xaa.csv, NeurIPS2010xab.csv,...]
        self.path_lst = [] #list of pathways to csv files

        #initializes list of paths to csvs
        self.data_lst = self.get_data()

        #initializes dataset to be read
        self.data = pd.read_csv(self.data_lst[0]) 

        #initializes new column for the gender of the first/last author
        self.data['first-gender'] = ""
        self.data['last-gender'] = ""


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
    def get_data(self):

        #gets combined csv list
        self.combine_list()
        counter = 0

        #iterates over combined csv list and appends path to each csv in a new array
        for i in self.combined_lst:
            self.path_lst.append(self.path+"\\Affiliation_Parsing\\"+self.affiliation_type(self.affiliation_year(self.combined_lst[counter]))+" affiliations gender\\"+self.affiliation_year(self.combined_lst[counter])+"\\"+self.combined_lst[counter])
            counter+=1

        return self.path_lst

    #recieves online link to search for pronouns, returning a gender label
    def findGender(self, urlLink):
        gender = ''
        ## put a url where the desciption of the author is avilable
        url = urlLink
        htmlText = requests.get(url).text
        soup = BeautifulSoup(htmlText, 'html.parser')


        # gathers all the p tags from the html
        soupstring = str(soup.find_all("p"))
        shetags = [" she ", " She "," her ", " Her "," hers "," Hers "]
        hetags = [" he ", " He "," his ", " His "," him "," Him "]
        theytags = [" they ", "They ", " them ", "Them " ]

        ##checks if male or female pronouns are present in the desciption
        containsfemale = any(femalepronouns in soupstring for femalepronouns in shetags)
        containsmale = any(malepronouns in soupstring for malepronouns in hetags)
        containsthey = any(theypronouns in soupstring for theypronouns in theytags)
        
        if containsfemale:
            gender = "Female"
        elif containsmale:
            gender = "Male"
        #     elif containsthey:
#         gender = "they/them"
        else:
            gender = "Undefined"
        return gender



    #returns whether or not a substring exists in a string
    def substring_exists(self, string, sub_string):
        return string.find(sub_string)

    #returns a list of the first-authors
    def getFirstAuthorList(self):
        for column in self.data[['first-author']]:
            authors = self.data[column]

            '''
            Prints out column name and its values
            '''
            #print('Column Name: '+column)
            #print(authors.values)

        lst_authors = authors.values
        return lst_authors


    #fills in gender column for first-author column
    def genderFirstAuthor(self):

        #initializes counter that keep track of author index
        counter = 0

        #gets list of the first authors
        lst=self.getFirstAuthorList()

        #loops through each author in the dataset
        for person in lst:

            '''
            search term for googlesearch
            follows structure of author's name, their affiliation, and .edu
            i.e. Glendon Chin Steven's Institute of Technology .edu
            '''
            query=person+" "+self.data['first-author-affiliation'].values[counter]+" .edu"


            
            #gets multiple links based on the search term
            for link in search(query, tld="co.in", num=5, stop=5, pause=2):
                
                unwantedLinks = ["pdf", "dblp"]

                
                #if the link is not .edu, we will not use that link
                if(self.substring_exists(link, ".edu")!=-1 or self.substring_exists(link, ".org")!=-1):
                    containsUnwanted = any(elements in link for elements in unwantedLinks)

                    gender_first_author = self.findGender(link)
                    if(containsUnwanted==False and (gender_first_author=="Male" or gender_first_author=="Female")):
                        self.data['first-gender'].values[counter]=gender_first_author
                        print("Link used for "+self.data['first-author'].values[counter]+": "+link)
                        break
                    # print("Author: "+self.data['first-author'].values[counter])
                    # print("Affiliation: "+self.data['first-author-affiliation'].values[counter])
                    # print("Gender: "+self.data['first-gender'].values[counter])
                    # print("Counter: "+str(counter))
                    # print("Link: "+link)
                    # print()
                else:
                    #print("Skipped "+link)
                    pass
            
            #increments index, moves to the next row
            counter+=1



    def test(self):
        return self.data

obj = Gender()
obj.genderFirstAuthor()
print(obj.test())
#print(obj.FirstAuthorGender())
#imports pandas to read in data
import pandas as pd

#imports BS4 libraries for webscraping
from re import I
import requests
from bs4 import BeautifulSoup

#imports googlesearch to use requests and BS4 to scrape google
from googlesearch import search

#reads in data
data = pd.read_csv(r"Affiliation_Parsing\NeurIPS affiliations gender\NeurIPS-2010\xaa.csv")

class Gender:

    #initializes new column for the gender of the first/last author
    data['first-gender'] = ''
    data['last-gender'] = ''

    def __init__(self, data):
        self.data = data

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

        ##checks if male or female pronouns are present in the desciption
        containsfemale = any(femalepronouns in soupstring for femalepronouns in shetags)
        containsmale = any(malepronouns in soupstring for malepronouns in hetags)

        #insert they tags
        
        if containsfemale:
            gender = "female"
        elif containsmale:
            gender = "male"
        else:
            gender = "undefined"
        return gender



    #returns whether or not a substring exists in a string
    def substring_exists(self, string, sub_string):
        return string.find(sub_string)

    #returns a list of the first-authors
    def getFirstAuthorList(self):
        for column in data[['first-author']]:
            authors = data[column]

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
            query=person+" "+data['first-author-affiliation'].values[counter]+" .edu"


            
            #gets multiple links based on the search term
            for link in search(query, tld="co.in", num=5, stop=5, pause=2):
                print("test link: "+link)

                #if the link is not .edu, we will not use that link
                if(self.substring_exists(link, ".edu")!=-1):
                    data['first-gender'].values[counter]=self.findGender(link)
                    print("Author: "+data['first-author'].values[counter])
                    print("Affiliation: "+data['first-author-affiliation'].values[counter])
                    print("Gender: "+data['first-gender'].values[counter])
                    print("Counter: "+str(counter))
                    print("Link: "+link)
                    print()
                    break
                else:
                    print("Skipped "+link)
            print()
            
            #increments index, moves to the next row
            counter+=1



g = Gender(data)
g.genderFirstAuthor()
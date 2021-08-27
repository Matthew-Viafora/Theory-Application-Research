# DESCRIPTION: This script parses through the Nuerips website shown below in the code and exports a csv file with the affiliations scraped from the url.

from csv import DictReader
import requests
from bs4 import BeautifulSoup
import os
import PyPDF2
import urllib.request
import io
import pandas as pd
import re

path = os.path.dirname(os.path.abspath(__file__))

year = '2020'

cols = ['first-author', 'first-author-affiliation', 'last-author', 'last-author-affiliation', 'title']
rows = []

nuerips_url = 'https://neurips.cc/Conferences/2020/Schedule?type=Poster'

html = requests.get(nuerips_url)
soup = BeautifulSoup(html.content, 'html.parser')

results = soup.find(id='main')

tags = results.find_all('div')
paper_count = 0
for tag in tags:
    # if paper_count == 10:
    #     break
    # else:
        try:

            paper_title_target = tag.find('div', class_ = 'maincardBody')
            paper_title = paper_title_target.text


            onclick = tag['onclick']


            paper_tag_url = 'https://neurips.cc/Conferences/2020/Schedule?showEvent=' + onclick[11:15]
            html_2 = requests.get(paper_tag_url)
            soup_2 = BeautifulSoup(html_2.content, 'html.parser')



            results_2 = soup_2.find('div',attrs={'class':'col-xs-12 col-sm-9'})


            
            tags_2 = results_2.find_all('button')


            # print(paper_tag_url)
            # print(results_2)
            # print(tags_2)
            # break



            author_tag_first = None
            author_tag_last = None
            temp = None
            count = 0
            for tag_2 in tags_2:
                if count == 0:
                    author_tag_first = tag_2['onclick']
                    count +=1
                temp = tag_2['onclick']
            author_tag_last = temp

            
            # print(author_tag_first)
            # print(author_tag_last)

            number_regex_first = re.findall(r'\d+\-\d+', author_tag_first)
            number_regex_last = re.findall(r'\d+\-\d+', author_tag_last)


            first_author_url = 'https://neurips.cc/Conferences/2020/Schedule?showSpeaker=' + number_regex_first[0]
            last_author_url = 'https://neurips.cc/Conferences/2020/Schedule?showSpeaker=' + number_regex_last[0]

        

            html_request_first = requests.get(first_author_url)
            html_request_last = requests.get(last_author_url)
            soup_first = BeautifulSoup(html_request_first.content, 'html.parser')
            soup_last = BeautifulSoup(html_request_last.content, 'html.parser')
            results_first = soup_first.find(id='whaat')
            results_last = soup_last.find(id='whaat')
            
            affiliation_first_target = results_first.find('h4')
            affiliation_last_target = results_last.find('h4')
            name_first_target = results_first.find('h3')
            name_last_target = results_last.find('h3')

            name_first = name_first_target.text
            name_last = name_last_target.text
            affiliation_first = affiliation_first_target.text
            affiliation_last = affiliation_last_target.text

            

            # print("______________________________________________________________________________")
            # print("Paper: " + paper_title)
            # print()
            # print("First author: " + name_first)
            # print("First author affiliation: " + affiliation_first)
            # print()
            # print("Last author: " + name_last)
            # print("Last author affiliation: " + affiliation_last)
            # print("______________________________________________________________________________")


            rows.append({"first-author" : name_first,
                         "first-author-affiliation" : affiliation_first,
                         "last-author" : name_last,
                         "last-author-affiliation" : affiliation_last,
                         "title" : paper_title})
            paper_count+=1
            print(paper_count)

        except:
            continue

df = pd.DataFrame(rows, columns=cols)
df.to_csv(path+year+'output.csv')
       


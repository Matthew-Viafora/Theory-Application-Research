from csv import DictReader
import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

path = os.path.dirname(os.path.abspath(__file__))

cols = ['first-author-affiliation','last-author-affiliation', 'title']
rows = []

##########################################User Input#####################################
########################################################################################
year = '2017'
num_heading = '3'
IJCAI_url = 'https://dl.acm.org/doi/proceedings/10.5555/3298483?tocHeading=heading3'
#########################################################################################


html = requests.get(IJCAI_url)
soup = BeautifulSoup(html.content, 'html.parser')

results = soup.find(id='pb-page-content')

container = results.find_all("h5", class_="issue-item__title")

paper_count = 0


links_with_text = []
for a in container:
    links = a.find_all("a")
    for link in links:
        link_url =link['href']
        links_with_text.append(link_url)


for paper in links_with_text:
    try:
        paper_url = 'https://dl.acm.org'+paper
        html_affil = requests.get(paper_url)
        soup_affil = BeautifulSoup(html_affil.content, 'html.parser')
        results_affil = soup_affil.find(id='sb-1')
        results_affil_title = soup_affil.find(id='pb-page-content')
        pill_info = results_affil.find_all("span", class_='loa_author_inst')
        titles = results_affil_title.find_all("h1", class_='citation__title')
        
        article_title = None
        for title in titles:
            article_title = title.text
        


        author_affiliations = []
        for info in pill_info:
            author_affiliations.append(info.text)

        first_author_affiliation = author_affiliations[0]
        last_author_affiliation = author_affiliations[-1]

        # print("_______________")
        # print("first author affiliation: ",first_author_affiliation)
        # print("last author affiliation",last_author_affiliation)
        # print("_______________")

        rows.append({"first-author-affiliation" : first_author_affiliation,
                            "last-author-affiliation" : last_author_affiliation,
                            "title" : article_title})

        paper_count+=1
        print(paper_count)
        print(article_title)
    except:
        continue



df = pd.DataFrame(rows, columns=cols)
df.to_csv(path+year+'_'+num_heading+'_output.csv')

print('CSV #'+num_heading)
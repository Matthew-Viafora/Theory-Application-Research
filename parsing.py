# Theory, Application, and Gender in research
# Matthew Viafora, Jhanvi Ganesh, Glendon Chin, Harrison Chachko
# Last updated: 6/7/21
import xml.etree.ElementTree as ET
import os
import pandas as pd


count = 0

# Current file path
path = os.path.dirname(os.path.abspath(__file__))

# List of folders to iterate over
folders = ["IJCAI-XML", "MLHC-XML", "NeurIPS-XML", "AAAI-XML", "ICML-XML"]

# Iterate over folders
for folder in folders:
    file_arr = os.listdir(path+'/'+folder)

    # Iterate over files in that folder
    cols = ["year","first-author","last-author","journal/conference","title","number-of-authors", "paper-url", "DBLP-url"]
    rows = []
    for file in file_arr:
        # Parsing the XML file
        xmlparse = ET.parse(path+'/'+ folder+'/'+file)

        root = xmlparse.getroot()
        for i in root.iter("info"):
            # Get attributes
            title = getattr(i.find("title"), 'text', "nan")
            year = getattr(i.find("year"), 'text', "nan")
            conference = getattr(i.find("venue"), "text", "nan")
            paper_url = getattr(i.find("ee"), "text", "nan")
            DBLP_url = getattr(i.find("url"), "text", "nan")

            # Get author count and first/last authors
            author_count = 0
            last_child = None

            if i.find("authors") != None:
                for child in i.find("authors"):
                    if author_count == 0:
                        first_author = child.text
                    author_count+=1
                    last_child = child
                last_author = last_child.text
            else:
                count+=1
            
            # Append all attributes to csv
            rows.append({"year" : year, 
                        "number-of-authors" : author_count, 
                        "title" : title, 
                        "first-author" : first_author, 
                        "last-author" : last_author,
                        "journal/conference" : conference,
                        "paper-url" : paper_url,
                        "DBLP-url" : DBLP_url}) 

    df = pd.DataFrame(rows, columns=cols)
# Writing pandas dataframe to csv
    df.to_csv('/Users/mattviafora/Library/Mobile Documents/com~apple~CloudDocs/GitHub/Python Data Science/Theory-Application-Research/'+ folder +'-output.csv')
print("Total number of papers disregarded due to no authors:",count)

# Theory, Application, and Gender in research
# Matthew Viafora, Jhanvi Ganesh, Glendon Chin, Harrison Chachko
# Last updated: 6/7/21
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse
import os
import pandas as pd
from urllib.request import urlopen


waiting = 0
count = 0

# Current file path
path = os.path.dirname(os.path.abspath(__file__))

# List of folders to iterate over
# folders = ["IJCAI-XML", "MLHC-XML", "NeurIPS-XML", "AAAI-XML", "ICML-XML"]
folders = ['1']

# Iterate over folders
for folder in folders:
    file_arr = os.listdir(path+'/'+folder)

    # Iterate over files in that folder
    cols = ["year","first-author","first-author-affiliation","last-author","last-author-affiliation","journal/conference","title","number-of-authors", "paper-url", "DBLP-url"]
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
            xml_path_first = None

            if i.find("authors") != None:
                for child in i.find("authors"):
                    if author_count == 0:
                        first_author = child.text

                        # pid of first author
                        pid_first = child.attrib['pid']

                        #xml url to first author bio
                        xml_path_first = "http://dblp.org/pid/"+pid_first+".xml"
                    author_count+=1
                    last_child = child
                last_author = last_child.text

                # pid of last author
                pid_last = last_child.attrib['pid']

                # xml url to last author
                xml_path_last = "http://dblp.org/pid/"+pid_last+".xml"
            else:
                count+=1

            # print("______________________________________________________________")
            # print("URL: ",xml_path_last)
            # print("______________________________________________________________")

            # Open XML url and parse through to find "note" which is attatched to affiliation for first author
            first_author_affiliation = None
            
            try:
                first_var_url = urlopen(xml_path_first)
            except:
                count+=1
                continue
                
                
            author_parse = parse(first_var_url)

            first_author_root = author_parse.getroot()
            for person in first_author_root.iter("person"):
                first_author_affiliation = getattr(person.find("note"), 'text', 'nan')
                break
            
            # Open XML url and parse through to find "note" which is attatched to affiliation for last author
            last_author_affiliation = None
            
            try:
                last_var_url = urlopen(xml_path_last)
            except:
                count+=1
                continue
                
            last_author_parse = parse(last_var_url)

            last_author_root = last_author_parse.getroot()
            for person in last_author_root.iter("person"):
                last_author_affiliation = getattr(person.find("note"), 'text', 'nan')
                break

            waiting+=1
            print(waiting)
            
            # print("______________________________________________________________")
            # print("Name: ",last_author)
            # print("Affiliation: ", last_author_affiliation)


            # Append all attributes to csv
            rows.append({"year" : year, 
                        "number-of-authors" : author_count, 
                        "title" : title, 
                        "first-author" : first_author, 
                        "last-author" : last_author,
                        "journal/conference" : conference,
                        "paper-url" : paper_url,
                        "DBLP-url" : DBLP_url,
                        "first-author-affiliation" : first_author_affiliation,
                        "last-author-affiliation" : last_author_affiliation}) 

    df = pd.DataFrame(rows, columns=cols)
# Writing pandas dataframe to csv
    df.to_csv(path+ folder +'-output.csv')
print("Total number of papers disregarded due to errors:",count)

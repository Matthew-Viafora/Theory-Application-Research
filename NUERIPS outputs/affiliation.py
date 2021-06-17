from csv import DictReader
import requests
from bs4 import BeautifulSoup
import os
import PyPDF2
import urllib.request
import io

# First make sure all imports are working ^^^
# Change file path below to match your computer... should be the file path a NuerIPS CSV file (get NeurIPS outputs from github folder "NUERIPS outputs")
# The part of the code that extracts and prints out the text from the PDF is marked with #######

conference = 'NeurIPS'

with open('/Users/mattviafora/Library/Mobile Documents/com~apple~CloudDocs/GitHub/Python Data Science/Theory-Application-Research/NUERIPS outputs/NeurIPS-XML4-output.csv', 'r') as read_obj:
    csv_reader = DictReader(read_obj)

    # For each row (paper) in CSV
    for row in csv_reader:
        search = None
        if row['journal/conference'] == conference:
            search = row['paper-url']
        else:
            continue

        html = requests.get(search)
        soup = BeautifulSoup(html.content, 'html.parser')
        tags = soup('a')

        for i, tag in enumerate(tags):
            ans = tag.get('href',None)
            if i == 7:

                # LINK OF THE PDF OF THE PAPER
                link = "https://proceedings.neurips.cc/"+ans
                
                req = urllib.request.Request(link)
                remote_file = urllib.request.urlopen(req).read()
                remote_file_bytes = io.BytesIO(remote_file)
                pdfReader = PyPDF2.PdfFileReader(remote_file_bytes)
                
                ###################################################
                # gets the first page of the pdf and prints out the text of the pdf
                pageObj = pdfReader.getPage(0)
                print(pageObj.extractText())
                ###################################################



                break

        #Delete this line to run on whole csv instead of just row (paper) \/\/\/
        break    

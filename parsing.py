# Theory, Application, and Gender in research
# Matthew Viafora, Jhanvi Ganesh, Glendon Chin, Harrison Chachko
# 6/4/21
import xml.etree.ElementTree as ET
import pandas as pd

# Create rows and columns for csv
cols = ["author", "title", "venue", "year", "url"]
rows = []

# Parsing the XML file
xmlparse = ET.parse('/Users/mattviafora/Library/Mobile Documents/com~apple~CloudDocs/GitHub/Python Data Science/Theory-Application-Research/34_test.xml')
root = xmlparse.getroot()
for i in root.iter("info"):
    title = getattr(i.find("title"), 'text', "nan")
    rows.append({ "title" : title})

df = pd.DataFrame(rows, columns=cols)

# Writing pandas dataframe to csv
df.to_csv('/Users/mattviafora/Library/Mobile Documents/com~apple~CloudDocs/GitHub/Python Data Science/Theory-Application-Research/output.csv')

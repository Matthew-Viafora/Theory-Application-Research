# Theory-Application-Research

Analyzing theory, application, and gender in research
________________________________________

## Overview

**Final Gender-Affiliation contains:**
- The final csv data for MLHC, ICML, and NeurIPS conferences (includes first/last author affiliations and their gender)
- 

**Affiliation_Parsing contains:**
- All csvs from NeurIPS, ICMl, MLHC, AAAI, and the the respective affiliations of the authors in each dataset
- The sub affiliations gender folders contain the same data as the affiliations folder, separated into multiple files of <= 20 rows of data

**NeurIPS-XML contains:**
- All paper information from 2010-2020 NeurIPS conference in XML files (Advances in Neural Information Processing Systems ##: Annual Conference on Neural Information Processing Systems)
- In more recent years (2018-2020), the amount of papers surpasses 1,000 and dblp only allows for 1,000 papers per XML file so there may be some papers missing in 2018-2020
- All papers are from "advances in neural information processsing systems..." I think that the other topics "proceedings, workshop, etc. may be application while the main one "advances in neural infromation processing..." is theory... so everything in this folder should be theory


**ICML-XML contains:**
- All paper information from 2010-2020 ICML conference in XML files 
- Since we want to use only theoritcal data from ICML, I was unsure if we wanted to use all of the files of certain conferences that had multiple.

**MLHC-XML contains:**
- All paper information from 2010-2020 MLHC conference in XML files

**AAAI-XML contains:**
- All paper information from 2010-2020 AAAI conference in XML files
- Was unsure if all the files under the AAAI needed to be uploaded or if only files containing AAAI needed to be uploaded

**IJCAI-XML contains:**
- ALl paper information from 2010-2020 IJCAI conference in XML files
- XML files are labeled in ascending order from most recent conference (i.e. 1.xml is from 35th AAAI / 33nd IAAI 2021)

**parsing.py contains:**
- Python script to parse XML files for specified fields

**parsing_V2.py contains:**
- Python script to parse XML files for specified fields
- Added support for affiliation from DBLP

**Output-CSVs contains:**
- CSV files containing data parsed from XML files
- CSV files are sorted by conference

**gender.py contains:**
- Python script to iterate over affiliation csv folders and its contents
- Python script to webscrape for an authors gender

**dataAnalysis.ipynb contains:**
- Notebook to check datasets, identify potential issues, clean data

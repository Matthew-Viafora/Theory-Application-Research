# Theory-Application-Research

Analyzing theory, application, and gender in research
________________________________________

## Overview

**NeurIPS-XML contains:**

- All paper information from 2010-2020 NeurIPS conference in XML files (Advances in Neural Information Processing Systems ##: Annual Conference on Neural Information Processing Systems)
- In more recent years (2018-2020), the amount of papers surpasses 1,000 and dblp only allows for 1,000 papers per XML file so there may be some papers missing in 2018-2020
- XML files in folder are organized as "(conference number)"
- All papers are from "advances in neural information processsing systems..." I think that the other topics "proceedings, workshop, etc. may be application while the main one "advances in neural infromation processing..." is theory... so everything in this folder should be theory


**ICML-XML contains:**
- All paper information from 2010-2020 ICML conference in XML files 
- XML files in folder are organized as "(conference number)"
- Since we want to use only theoritcal data from ICML, I was unsure if we wanted to use all of the files of certain conferences that had multiple. If there is a "-1" in the file name, there are multiple files from that year, so we should review which file(s) to use

**MLHC-XML contains:**
- All paper information from 2010-2020 MLHC conference in XML files
- XML files in folder are organized as MLHC with the corresponding year of the conference

**AAAI-XML contains:**
- All paper information from 2010-2020 AAAI conference in XML files
- XML files in folder are organized as their conference number along with AAAI and the corresponding year of the conference
- Was unsure if all the files under the AAAI needed to be uploaded or if only files containing AAAI needed to be uploaded

***IJCAI-XML contains:**
- ALl paper information from 2010-2020 IJCAI conference in XML files
- XML files are labeled in ascending order from most recent conference (i.e. 1.xml is from 35th AAAI / 33nd IAAI 2021)

**parsing.py:**
- Python script to parse XML files for specified fields

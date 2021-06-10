

from re import I
import requests
from bs4 import BeautifulSoup
gender = ''
## put a url where the desciption of the author is avilable
url = 'https://www.microsoft.com/applied-sciences/people/saeed-amizadeh'
htmlText = requests.get(url).text
soup = BeautifulSoup(htmlText, 'html.parser')
# gathers all the p tags from the html
soupstring = str(soup.find_all("p"))
shetags = [" she ", " She "," her ", " Her "," hers "," Hers "]
hetags = [" he ", " He "," his ", " His "," him "," Him "]
##checks if male or female pronouns are present in the desciption
containsfemale = any(femalepronouns in soupstring for femalepronouns in shetags)
containsmale = any(malepronouns in soupstring for malepronouns in hetags)

if containsfemale:
    gender = "female"
else:
    gender = "male"
print(gender)



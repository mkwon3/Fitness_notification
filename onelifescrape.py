#To use this code, you will first need to install the two packagtes being imported below using pip or manual install method.

from bs4 import BeautifulSoup
import requests

#grab basic content from a web page
url = "https://www.onelifefitness.com/gyms/atlanta-holly-springs?hsLang=en"
page = requests.get(url)

#using the lxml parser to process the webpage text content
soup = BeautifulSoup(page.content,'html.parser')

lists = soup.find_all('section', id="schedule")

#make a loop to find the class_name of each section
for list in lists:
    class_name = list.find('img', alt="Les Mills BODYPUMP™")
    info = [class_name]
    print(info)
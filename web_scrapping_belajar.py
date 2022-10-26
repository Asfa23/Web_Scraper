import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.unair.ac.id/news/')

#requests 
page.text

#BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

job_elements =  soup.find_all("div", class_="elementor-button-wrapper")

for x in job_elements:
    print(x, end="\n"*2)
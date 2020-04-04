import requests
from bs4 import BeautifulSoup, Comment

URL = "https://www.basketball-reference.com/teams/TOR/2020.html"
r = requests.get(url = URL)

html_doc = r.text

soup = BeautifulSoup(html_doc, 'html.parser')
table = soup.find(id="all_salaries2")
new_html = ''
new_html = table.find(text=lambda text:isinstance(text, Comment))
table_soup = BeautifulSoup(new_html, 'html.parser')
salaries = table_soup.findAll('td', class_="right")
names = table_soup.findAll('td', class_="left")

print(salaries)
print(names)

#TODO Partially done getting this data out of the comment that somehow shows the table
#Another option to explore using a similar method is to get the data from the player information table
#It's probably easier that way since then I dont have to figure out how to loop through every team in the league

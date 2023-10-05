from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(start_url)
soup = bs(page.text,'html.parser')
table = soup.find('table')

temp_list= []

rows = table.find_all('tr')

for tr in rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]
Lum = []

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])
    
data = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(data)

data.to_csv('final_1.csv')
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)
soup = bs(page.text,'html.parser')
table = soup.find_all('table')

temp_list= []

rows = table[7].find_all('tr')

for tr in rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_Names = []
Distance =[]
Mass = []
Radius =[]

for i in range(1,len(temp_list)):
    
    Star_Names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

data = pd.DataFrame(list(zip(Star_Names,Distance,Mass,Radius,)),columns=['Star Name','Distance','Mass','Radius'])
print(data)

data.to_csv('final_2.csv')
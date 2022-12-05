import requests
from bs4 import BeautifulSoup
import pandas as pd
dic={}

if __name__ == "__main__":
    url = requests.get('https://www.2026worldcupnorthamerica.com/fifa-ranking/')
    soup = BeautifulSoup(url.text, 'html.parser')
    main = soup.find('main',attrs={'id':'main', 'class':'site-main'})
    container = main.find('div',attrs={'class':'inside-article'})
    body = container.find('tbody')
    data = body.find_all('tr')
    
    id = []
    rankings = []
    countries= []
    points = []
    i = 0
    # now we got all our data  
    for row in data:
      columns = row.find_all('td')
      ranking = columns[0].find('strong').text.strip()
      country = columns[1].find('strong').text.strip()
      point = columns[2].find('strong').text.strip()
        
      id.append(i)
      rankings.append(ranking)
      countries.append(country)      
      points.append(point)
      i = i + 1
    
    dic = {'rankings': rankings, 'countries': countries, 'points': points}
    df = pd.DataFrame(dic)
    to_cv = df.to_csv('/mnt/c/users/weice/OneDrive/Desktop/wcp/data/datafiles/rankings.csv')

         


   
    
    
    
    
import requests
from bs4 import BeautifulSoup
import pandas as pd

dic={}

if __name__ == "__main__":
    url = requests.get('https://www.kaggle.com/datasets/abecklas/fifa-world-cup')
    soup = BeautifulSoup(url.text, 'html.parser')
    main = soup.find('main')
    container = main.find('div', attrs={'id':'site-content'})
    code = container.find('div', attrs={'class':'sc-bAKPPm fyNSfj'})
    dataset = container.find('div', attrs={'class':'sc-cbFqep hhZCSr'}).find('div', attrs={'class':'sc-iVxNgP iDiFlu'})
    data = container.find('div', attrs={'class':'sc-cBOWjd cjSlfu'})
    dar = data.find('div').find_all('span', attrs={'class':'sc-cTQhss sc-jOrMOR jMMnle dYzUGm'})
    
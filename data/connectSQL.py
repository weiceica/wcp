import requests
import mysql.connector
import pandas as pd

if __name__ == "__main__":
  data = pd.read_csv("./datafiles/WorldCupMatches.csv")
  df = pd.DataFrame(data, columns=['Home Team Name', 'Home Team Goals', 'Away Team Goals', 'Away Team Name'])
  df.to_csv("./datafiles/WorldCupMatchesSorted.csv")
  
  
  
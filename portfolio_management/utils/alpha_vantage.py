
import requests
import pandas as pd
import os

def get_alpha_vantage_tickers():
    API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
    url = f'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={API_KEY}'
    
    response = requests.get(url)
    if response.status_code == 200:
        with open('tickers_alpha.csv', 'w') as file:
            file.write(response.text)
        print("Saved Alpha Vantage tickers to tickers_alpha.csv")

        df = pd.read_csv('tickers_alpha.csv')
        tickers = df['symbol'].dropna().tolist()
        print(f"Extracted {len(tickers)} tickers from Alpha Vantage")
        return tickers
    else:
        print(f"Failed to fetch tickers from Alpha Vantage. Status code: {response.status_code}")
        return []

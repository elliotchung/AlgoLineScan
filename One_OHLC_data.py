import requests
import json

access_token = "" # Replace with your own access token
symbol = "TSLA" # Replace with the stock symbol you're interested in
start_date = "2018-02-22" # Replace with the start date of the data range you're interested in
end_date = "2023-02-22" # Replace with the end date of the data range you're interested in
interval = "daily" # Specify the frequency of the data (e.g., daily or weekly)

url = f"https://api.tradier.com/v1/markets/history?symbol={symbol}&interval={interval}&start={start_date}&end={end_date}"
headers = {"Authorization": f"Bearer {access_token}", 'Accept': 'application/json'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = json.loads(response.text)
    # The OHLC data will be contained in the 'history' field of the response
    ohlc_data = data["history"]
    #print(ohlc_data)
else:
    print(f"Error retrieving data: {response.status_code}")

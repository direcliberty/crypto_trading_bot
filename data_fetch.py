
import requests

# Функция для получения данных с Binance API
def fetch_data():
    url = 'https://api.binance.com/api/v3/ticker/price'
    coins = ['BTCUSDT', 'ETHUSDT', 'XRPUSDT']

    data = {}
    for coin in coins:
        response = requests.get(url, params={'symbol': coin})
        if response.status_code == 200:
            data[coin] = response.json()['price']

    return data

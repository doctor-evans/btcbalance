from django.shortcuts import render
import requests
from bs4 import BeautifulSoup




BLOCKCHAIN_URL = 'https://www.blockchain.com/search?search={}'
BITCOIN_URL = 'https://www.blockchain.com/btc/address/{}'
ETHERUM_URL = 'https://www.blockchain.com/eth/address/{}'
live_url = 'https://cryptowat.ch/'

# Create your views here.


def home(request):
    res2 = requests.get(live_url)
    soup2 = BeautifulSoup(res2.text, features='html.parser')
    live_price = soup2.find_all('span', {'class': '_3XNm6CSrchU-MNbu1Zh3m2'})
    live_bitcoin_price = f'{float(live_price[0].getText()):,}'
    price = live_price[1].getText()
    current_price_eth = f'{float(price):,}'
    context = {
        'live_bitcoin_price': live_bitcoin_price,
        'current_price_eth': current_price_eth,
    }
    return render(request, 'btc/home.html', context)

def check(request):
    res2 = requests.get(live_url)
    soup2 = BeautifulSoup(res2.text, features='html.parser')
    live_price = soup2.find_all('span', {'class': '_3XNm6CSrchU-MNbu1Zh3m2'})
    live_bitcoin_price = f'{float(live_price[0].getText()):,}'
    btc_price = live_price[0].getText()
    price = live_price[1].getText()
    current_price_eth = f'{float(price):,}'

    address = request.POST.get('address')
    type = request.POST.get('crytotype')
    if type == "BTC":
        try:
            final_url = BITCOIN_URL.format(address)
            response = requests.get(final_url)
            data = response.text
            soup = BeautifulSoup(data, features='html.parser')
            balance = soup.find_all('span', {'class': 'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
            btc_balance = balance[4].getText()
            btc = btc_balance.split(' ')
            usd_balance1 = float(btc[0]) * float(btc_price)
            usd_balance = f'{float(usd_balance1):,}'
        except Exception as e:
            raise e
    elif type == "ETH":
        try:
            final_url = ETHERUM_URL.format(address)
            response = requests.get(final_url)
            data = response.text
            soup = BeautifulSoup(data, features='html.parser')
            balance = soup.find_all('span', {'class': 'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
            btc_balance = balance[3].getText()
            btc = btc_balance.split(' ')
            usd_balance1 = float(btc[0]) * float(btc_price)
            usd_balance = f'{float(usd_balance1):,}'
        except Exception as e:
            raise e


    context = {
        'type' : type,
        'address' : address,
        'live_bitcoin_price': live_bitcoin_price,
        'current_price_eth': current_price_eth,
        'btc_balance' : btc_balance,
        'usd_balance' : usd_balance
    }
    return render(request, 'btc/check.html', context)

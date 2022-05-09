import streamlit as st
import json
import requests

with open('cryptocurrencies.json', 'r') as file:
    data = json.loads(file.read())

def get_price(name):
    base_url = 'https://api.alternative.me/v2/ticker/'
    url = base_url + name + '/?convert=USD'
    response = requests.get(url).json()
    key = list(response['data'].keys())[0]
    price = response['data'][key]['quotes']['USD']['price']
    return price

def convert(amount, coin1, coin2):
    coin1_price = get_price(coin1)
    coin2_price = get_price(coin2)
    value_usd1 = coin1_price * amount
    value_usd2 = value_usd1 / coin2_price
    return value_usd2

test = ['BTC', 'ETH', 'USDC', 'ADA', 'LTC']

coin1_input = st.text_input('Choose first crypto', 'BTC')
coin2_input = st.text_input('Choose second crypto', 'ETH')
amount = st.slider('Choose the amount', 1,100)

coin1 = data[coin1_input]
coin2 = data[coin2_input]
st.write(convert(amount, coin1.lower().replace(" ", "-"), coin2.lower().replace(" ", "-")))
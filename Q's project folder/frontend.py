#Imported the libraries needed
import streamlit as st
import json
import requests

#In order to make the file cleaner we used a with statement to open the crytpocurrency json. We then created a variable and assigned it to load and read the file.
with open('cryptocurrencies.json', 'r') as file:
    data = json.loads(file.read())
    
#Defined the function that (TO BE CONTINUED)
def get_price(name):
    base_url = 'https://api.alternative.me/v2/ticker/'
    url = base_url + name + '/?convert=USD'
    response = requests.get(url).json()
    key = list(response['data'].keys())[0]
    price = response['data'][key]['quotes']['USD']['price']
    return price

#(TO BE CONTINUED)
def convert(amount, coin1, coin2):
    coin1_price = get_price(coin1)
    coin2_price = get_price(coin2)
    value_usd1 = coin1_price * amount
    value_usd2 = value_usd1 / coin2_price
    return value_usd2

#Created a list of crypto currencies that are accepted in the converter.
test = ['BTC', 'ETH', 'USDC', 'ADA', 'LTC']

#Created a variable for the first currency that the user wants to convert and a second variable for the first currency to be converted into. We also made streamlit fill in the first and second currencies by default until the user inouts his information.
coin1_input = st.text_input('Choose first crypto', 'BTC')
coin2_input = st.text_input('Choose second crypto', 'ETH')
amount = st.slider('Choose the amount', 1,100)

#Created two more variables for when the user inputs his own data. The converter will use the users given data to return the value instead of the default inputs given before.
coin1 = data[coin1_input]
coin2 = data[coin2_input]
st.write(convert(amount, coin1.lower().replace(" ", "-"), coin2.lower().replace(" ", "-")))
#Imported the libraries needed
import streamlit as st
import json
import requests

#In order to make the file cleaner we used a with statement to open the crytpocurrency json. We then created a variable and assigned it to load and read the file.
with open('cryptocurrencies.json', 'r') as file:
    data = json.loads(file.read())
    
#Defined the function "get_price" in order to accept the name parameter. Then we made several variables inside the function. In the "base_url" varaiable we referenced the endpoint url in order to seek information on certain cryptos. The "url" variable uses the endpoint url and the name of the crypto to convert into USD value. The "response" variable uses the get function to request data from the server. The "key" variable gets the keys from the dictionary in the json file. The "price" variable puts them all together in order to get the end product which we then return the value of.
def get_price(name):
    base_url = 'https://api.alternative.me/v2/ticker/'
    url = base_url + name + '/?convert=USD'
    response = requests.get(url).json()
    key = list(response['data'].keys())[0]
    price = response['data'][key]['quotes']['USD']['price']
    return price

#We defined the function "convert" in order to accept the parameters (amount, coin1, and coin2). This second defined function is used to convert the value of the first coin into the value of the second coin. The price of the cryptocurrency is retrieved but using the "get_price" function above. Then the "value_usd1" variable takes the price of the first coin and multiplies it by the amount the user has. The variable "value_usd2" takes the value from "value_usd1" and divides it by the variable "coin2_price". The result of "value_usd2" is returned. 
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

#Created two more variables for when the user inputs his own data. The converter will use the users given data to return the value instead of the default inputs given before when the Currency Converter first launched.
coin1 = data[coin1_input]
coin2 = data[coin2_input]
st.write(convert(amount, coin1.lower().replace(" ", "-"), coin2.lower().replace(" ", "-")))
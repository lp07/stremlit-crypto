import yfinance as yf
import streamlit as st
# python images library for the displaying different images for different concurrences
from PIL import Image
# Image is located on website or url
from urllib.request import urlopen

# Title and subtitles
st.title("Cryptocurrency Daily Prices")
st.header("Main Dashboard")
st.subheader("you can add more crypto in code </>")

# Defining ticker variables
Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Ripple = 'XRP-USD'
BitcoinCash = "BCH-USD"
Tether = "USDT-USD"

# Access data from Yahoo Finance
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(BitcoinCash)
USDT_Data = yf.Ticker(Tether)

# fetch history data from yahoo finance
BTCHis = BCH_Data.history(period="max")
ETHHis = ETH_Data.history(period="max")
XRPHis = XRP_Data.history(period="max")
BCHHis = BCH_Data.history(period="max")
USDTHis = USDT_Data.history(period="max")

# Fetch crypto data for the dataframe
BTC = yf.download(Bitcoin,
                  start="2023-05-20", end="2023-05-22")
ETH = yf.download(Ethereum,
                  start="2023-05-20", end="2023-05-22")
XRP = yf.download(Ripple,
                  start="2023-05-20", end="2023-05-22")
BCH = yf.download(BitcoinCash,
                  start="2023-05-20", end="2023-05-22")
USDT = yf.download(Tether,
                  start="2023-05-20", end="2023-05-22")

# Bitcoin
st.write("BITCOIN ($)")
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
# Displaying image
st.image(imageBTC)
# Displaying dataframe
st.table(BTC)
# Display a chart
st.bar_chart(BTCHis.Close)

# Ethereum
st.write("ETHEREUM ($)")
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
# Displaying image
st.image(imageETH)
# Displaying dataframe
st.table(ETH)
# Display a chart
st.bar_chart(ETHHis.Close)

# Ripple
st.write("RIPPLE ($)")
imageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
# Displaying image
st.image(imageXRP)
# Displaying dataframe
st.table(XRP)
# Display a chart
st.bar_chart(XRPHis.Close)

# BitcoinCash
st.write("BITCOINCASH ($)")
imageBCH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png'))
# Displaying image
st.image(imageBCH)
# Displaying dataframe
st.table(BCH)
# Display a chart
st.bar_chart(BCHHis.Close)

# Tether
st.write("TETHER ($)")
imageUSDT = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
# Displaying image
st.image(imageUSDT)
# Displaying dataframe
st.table(USDT)
# Display a chart
st.bar_chart(USDTHis.Close)


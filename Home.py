from st_on_hover_tabs import on_hover_tabs
import streamlit as st
st.set_page_config(layout="wide")


# HEADER
col1, col2, col3 = st.columns([1,3,1])
with col2:
  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:50px;text-align:center;text-shadow: 5px 5px black;color:#fe1f70;">{"Growth of Liqudity Providers"}</h1>', unsafe_allow_html=True)


# Declare CSS File
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Overview', 'Ethereum LPs', 'Ethereum 🆚 L2s'], 
                         iconName=['dashboard', 'money', 'economy'], default_choice=0)

if tabs =='Overview':
  from Overview import test
  test()

elif tabs == 'Ethereum LPs':
  from Ethereum_LPs import test
  test()

elif tabs == 'Ethereum 🆚 L2s':
  from Ethereum_vs_L2s import test
  test()
    
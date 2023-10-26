from st_on_hover_tabs import on_hover_tabs
import streamlit as st
st.set_page_config(layout="wide")

# st.image("https://altcoinsbox.com/wp-content/uploads/2022/12/uniswap-logo-banner.png")

st.markdown(f'<h1 style="background-image:url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR161CeyquZeVivKqosn-o7etI4ca0CG8kIexNzsB3BGmkE0CfrA_n8epPfyU7n5bZZz3E&usqp=CAU);font-weight:bold;font-family:Georgia;font-size:60px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;box-shadow: 3px 3px black;">{"Growth of Liqudity Providers"}</h1>', unsafe_allow_html=True)

# # HEADER
# col1, col2, col3 = st.columns([1,3,1])
# with col2:
#   st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:50px;text-align:center;text-shadow: 5px 5px black;color:#fe1f70;">{"Growth of Liqudity Providers"}</h1>', unsafe_allow_html=True)


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
    

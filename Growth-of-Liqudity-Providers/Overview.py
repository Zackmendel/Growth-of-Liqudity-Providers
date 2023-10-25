import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from millify import millify

from st_on_hover_tabs import on_hover_tabs
def test():
  # Styling of metric container
  st.markdown("""
  <style>
  div[data-testid="metric-container"] {
     background-color: #424b43;
     border: 3px solid #111212;
     padding: 5% 5% 5% 10%;
     border-radius: 10px;
     color: white;
     overflow-wrap: break-word;
  }

  /* breakline for metric text         */
  div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
     overflow-wrap: break-word;
     white-space: break-spaces;
     color: #B7e493;
  }
  </style>
  """, unsafe_allow_html=True)


  tab1, tab2 = st.tabs(["All-Time Data", "Past Month Data"])

  with tab1:
    st.header("All Time Trading Stats on Uniswap")
    col_1, col_2, col_3, col_4 = st.columns(4, gap='large')
    url_0 = "https://api.flipsidecrypto.com/api/v2/queries/24f569be-2967-477a-aec5-153652ba2d56/data/latest"
    df_0 = pd.read_json(url_0)
    with col_1:
      url_a = "https://api.flipsidecrypto.com/api/v2/queries/a54b2d6d-4306-4840-9d2d-39a10ffd90ef/data/latest"
      df_a = pd.read_json(url_a)
      st.metric(label="TVL Uniswap", value=(millify(df_a["BAL"][0], precision=2)))
    
    with col_2:
      st.metric(label="Total Volume Traded on Uniswap", value=(millify(df_0["VOLUME_USD"][0], precision=2)))
  
    with col_3:
      st.metric(label="Total Swap Count on Uniswap", value=(millify(df_0["SWAP_COUNT"][0], precision=2)))
  
    with col_4:
      st.metric(label="Total User Count on Uniswap", value=(millify(df_0["USERS_COUNT"][0], precision=2)))
  
  
    col_1, col_2, col_3 = st.columns(3, gap='large')
    url_1 = "https://api.flipsidecrypto.com/api/v2/queries/b936268f-f6b5-41ea-a741-540917b4eb6a/data/latest"
    df_1 = pd.read_json(url_1)
  
    url_2 = "https://api.flipsidecrypto.com/api/v2/queries/6b985d8c-a09e-4468-9d3b-6339b7d3ba70/data/latest"
    df_2 = pd.read_json(url_2)
  
    with col_1:
      fig_1 = px.bar(df_1, x="BLOCKCHAIN", y="VOLUME_USD", color="BLOCKCHAIN", title="1. Uniswap Trading Volume", height=400)
      fig_1.update_layout(hovermode="x unified")
      st.plotly_chart(fig_1, use_container_width=True)
  
      fig_2 = px.bar(df_2, x="TIMESPAN", y="VOLUME_USD", color="BLOCKCHAIN", title="Uniswap Monthly Trading Volume", height=400)
      fig_2.update_layout(hovermode="x unified")
      st.plotly_chart(fig_2, use_container_width=True)
  
    with col_2:
      fig_1a = px.bar(df_1, x="BLOCKCHAIN", y="SWAP_COUNT", color="BLOCKCHAIN", title="Uniswap Swap Count", height=400)
      fig_1a.update_layout(hovermode="x unified")
      st.plotly_chart(fig_1a, use_container_width=True)
  
      fig_2a = px.bar(df_2, x="TIMESPAN", y="SWAP_COUNT", color="BLOCKCHAIN", title="Uniswap Monthly Swap Count", height=400)
      fig_2a.update_layout(hovermode="x unified")
      st.plotly_chart(fig_2a, use_container_width=True)
  
    with col_3:
      fig_1b = px.bar(df_1, x="BLOCKCHAIN", y="USERS_COUNT", color="BLOCKCHAIN", title="Uniswap Swappers Count", height=400)
      fig_1b.update_layout(hovermode="x unified")
      st.plotly_chart(fig_1b, use_container_width=True)
  
      fig_2b = px.bar(df_2, x="TIMESPAN", y="USERS_COUNT", color="BLOCKCHAIN", title="Uniswap Monthly Swappers Count", height=400)
      fig_2b.update_layout(hovermode="x unified")
      st.plotly_chart(fig_2b, use_container_width=True)

  with tab2:
    st.header("Past Month Trading Stats on Uniswap")
    col_1, col_2, col_3 = st.columns(3, gap='large')
    url_0 = "https://api.flipsidecrypto.com/api/v2/queries/049c7e47-b730-44aa-9ee3-1dfd70550950/data/latest"
    df_0 = pd.read_json(url_0)
    with col_1:
      st.metric(label="Total Volume Traded on Uniswap(Past Month)", value=(millify(df_0["VOLUME_USD"][0], precision=2)))
  
    with col_2:
      st.metric(label="Total Swap Count on Uniswap(Past Month)", value=(millify(df_0["SWAP_COUNT"][0], precision=2)))
  
    with col_3:
      st.metric(label="Total User Count on Uniswap(Past Month)", value=(millify(df_0["USERS_COUNT"][0], precision=2)))
  
  
    col_1, col_2, col_3 = st.columns(3, gap='large')
    url_1 = "https://api.flipsidecrypto.com/api/v2/queries/fd826701-a84e-4a6e-bd66-d6fc16eb7f3c/data/latest"
    df_1 = pd.read_json(url_1)
  
    url_2 = "https://api.flipsidecrypto.com/api/v2/queries/1d5d5dec-2632-4055-887d-dea097b301e9/data/latest"
    df_2 = pd.read_json(url_2)
  
    with col_1:
      fig_1 = px.bar(df_1, x="BLOCKCHAIN", y="VOLUME_USD", color="BLOCKCHAIN", title="Uniswap Trading Volume(Past Month)", height=400)
      fig_1.update_layout(hovermode="x unified")
      st.plotly_chart(fig_1, use_container_width=True)
  
      fig_2 = px.bar(df_2, x="TIMESPAN", y="VOLUME_USD", color="BLOCKCHAIN", title="Uniswap Daily Trading Volume(Past Month)", height=400)
      fig_2.update_layout(hovermode="x unified")
      st.plotly_chart(fig_2, use_container_width=True)
  
    with col_2:
      fig_1a = px.bar(df_1, x="BLOCKCHAIN", y="SWAP_COUNT", color="BLOCKCHAIN", title="Uniswap Swap Count(Past Month)", height=400)
      fig_1a.update_layout(hovermode="x unified")
      st.plotly_chart(fig_1a, use_container_width=True)
  
      fig_2a = px.bar(df_2, x="TIMESPAN", y="SWAP_COUNT", color="BLOCKCHAIN", title="Uniswap Daily Swap Count(Past Month)", height=400)
      fig_2a.update_layout(hovermode="x unified")
      st.plotly_chart(fig_2a, use_container_width=True)
  
    with col_3:
      fig_1b = px.bar(df_1, x="BLOCKCHAIN", y="USERS_COUNT", color="BLOCKCHAIN", title="Uniswap Swappers Count(Past Month)", height=400)
      fig_1b.update_layout(hovermode="x unified")
      st.plotly_chart(fig_1b, use_container_width=True)
  
      fig_2b = px.bar(df_2, x="TIMESPAN", y="USERS_COUNT", color="BLOCKCHAIN", title="Uniswap Daily Swappers Count(Past Month)", height=400)
      fig_2b.update_layout(hovermode="x unified")
      st.plotly_chart(fig_2b, use_container_width=True)
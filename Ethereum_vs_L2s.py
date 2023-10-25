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

  st.header("LIQUIDITY PROVIDING(MINTING) ACTIVITIES ON UNISWAP")
  col_1, col_2, = st.columns([2,1])
  url_1 = "https://api.flipsidecrypto.com/api/v2/queries/c173391d-8bb9-4156-9dc1-ffc6ede23271/data/latest"
  df_1 = pd.read_json(url_1)

  with col_1:
    fig_1 = px.bar(df_1, x="TIMESPAN", y="LP_ADDING", color="CHAIN", title="Monthly Liquidity Providers(LP) Minting Across Chains", height=500)
    fig_1.update_layout(hovermode="x unified")
    st.plotly_chart(fig_1, use_container_width=True)

    fig_1a = px.bar(df_1, x="TIMESPAN", y="MINT_TX", color="CHAIN", title="Monthly Tx Count of Liquidity Provider(LP) Mint Actions Across Chains", height=500)
    fig_1a.update_layout(hovermode="x unified")
    st.plotly_chart(fig_1a, use_container_width=True)

  with col_2:
    fig_2 = px.pie(df_1, names="CHAIN", values="LP_ADDING", labels="CHAIN", title="Percent Liquidity Providers(LP) Minting Across Chains", height=500)
    fig_2.update_layout(hovermode="x unified")
    fig_2.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_2, use_container_width=True)
    
    fig_2a = px.pie(df_1, names="CHAIN", values="MINT_TX", labels="CHAIN", title="Percent Tx Count of Liquidity Provider(LP) Mint Actions Across Chains", height=500)
    fig_2a.update_layout(hovermode="x unified")
    fig_2a.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_2a, use_container_width=True)


  st.header("LIQUIDITY REMOVING(BURNING) ACTIVITIES ON UNISWAP")
  col_3, col_4, = st.columns([2,1])
  url_3 = "https://api.flipsidecrypto.com/api/v2/queries/37e532bd-3a0d-4c10-9448-82edac9da9cf/data/latest"
  df_3 = pd.read_json(url_3)

  with col_3:
    fig_3 = px.bar(df_3, x="TIMESPAN", y="LP_REMOVING", color="CHAIN", title="Monthly Liquidity Removers Across Chains", height=500)
    fig_3.update_layout(hovermode="x unified")
    st.plotly_chart(fig_3, use_container_width=True)

    fig_3a = px.bar(df_3, x="TIMESPAN", y="BURN_TX", color="CHAIN", title="Monthly Tx Count of Liquidity Provider(LP) Burn Actions Across Chains", height=500)
    fig_3a.update_layout(hovermode="x unified")
    st.plotly_chart(fig_3a, use_container_width=True)

  with col_4:
    fig_4 = px.histogram(df_3, x="CHAIN", y="LP_REMOVING", color="CHAIN", title="Percent Liquidity Removers Across Chains", height=500)
    fig_4.update_layout(hovermode="x unified")
    # fig_4.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_4, use_container_width=True)

    fig_4a = px.histogram(df_3, x="CHAIN", y="BURN_TX", color="CHAIN", title="Percent Tx Count of Liquidity Provider(LP) Burn Actions Across Chains", height=500)
    fig_4a.update_layout(hovermode="x unified")
    # fig_4a.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_4a, use_container_width=True)


  #Top 100 Liquidity Pools on Uniswap
  st.subheader("Top 100 Liquidity Pools on Uniswap")
  url_4 = "https://api.flipsidecrypto.com/api/v2/queries/8746d30d-cf24-42f3-9479-9414a1aae608/data/latest"
  df_4 = pd.read_json(url_4)
  st.dataframe(df_4, use_container_width=True)
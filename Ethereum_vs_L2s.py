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

  st.markdown("""
  ### This section is meant to track Liquidity Provider's activities across different chains, while comparing Ethereum to it's Layer 2 blockchains.

  ### Charts in this section are :red[not] set to update daily.
  """)

  

  st.header(":blue[LIQUIDITY PROVIDING(MINTING) ACTIVITIES ON UNISWAP]")

  

  st.subheader(":red[Grouped by Ethereum(Layer 1) and Layer 2]")

  col_1, col_2, = st.columns([2,1])
  url_1 = "https://api.flipsidecrypto.com/api/v2/queries/f6c516a5-8494-4848-a3cd-7b93e12fa359/data/latest"
  df_1 = pd.read_json(url_1)

  with col_1:
    fig_1 = px.histogram(df_1, x="TIMESPAN", y="LP_ADDING", color="CHAIN_TYPE", title="Monthly Liquidity Providers(LP) Minting L1 vs L2", barmode="group", height=500)
    fig_1.update_layout(hovermode="x unified")
    st.plotly_chart(fig_1, use_container_width=True)

    fig_1a = px.histogram(df_1, x="TIMESPAN", y="MINT_TX", color="CHAIN_TYPE", title="Monthly Tx Count of Liquidity Provider(LP) Mint Actions L1 vs L2", barmode="group", height=500)
    fig_1a.update_layout(hovermode="x unified")
    st.plotly_chart(fig_1a, use_container_width=True)

  with col_2:
    fig_2 = px.pie(df_1, names="CHAIN_TYPE", values="LP_ADDING", labels="CHAIN_TYPE", title="Percent Liquidity Providers(LP) Minting L1 vs L2", height=500)
    fig_2.update_layout(hovermode="x unified")
    fig_2.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_2, use_container_width=True)

    fig_2a = px.pie(df_1, names="CHAIN_TYPE", values="MINT_TX", labels="CHAIN", title="Percent Tx Count of Liquidity Provider(LP) Mint Actions L1 vs L2", height=500)
    fig_2a.update_layout(hovermode="x unified")
    fig_2a.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_2a, use_container_width=True)


  

  st.subheader(":red[Grouped by Chains]")
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


  st.markdown("""
  ### FINDINGS🔎
  - From our LPs minting(providing liquidity) and the minting transactions, we can see that Ethereum trumps all the L2s by having a 64% LPs providing liquidity, although historically speaking, L2s become more dominant in the early months of 2023, but lost pace in recent months.
  - While the L2s put up a good fight in terms of minting transactions completely dominating Ethereum in recent months and slightly leading Ethereum in overall percentage, 53%.
  - When grouped by chains, Arbitrum, Polygon and Optimism are seen to be the major competitors. Although this might be attributed to the fact that Uniswap only recently moved to the other chains. But one thing is for certain, the L2s adoption by LPs is positive.
  """)
  


  st.header(":blue[LIQUIDITY REMOVING(BURNING) ACTIVITIES ON UNISWAP]")

  

  st.subheader(":red[Grouped by Ethereum(Layer 1) and Layer 2]")
  col_3, col_4, = st.columns([2,1])
  url_3 = "https://api.flipsidecrypto.com/api/v2/queries/02c8e54a-c201-4776-bd38-50297491c039/data/latest"
  df_3 = pd.read_json(url_3)

  with col_3:
    fig_3 = px.bar(df_3, x="TIMESPAN", y="LP_REMOVING", color="CHAIN", title="Monthly Liquidity Removers L1 vs L2", height=500)
    fig_3.update_layout(hovermode="x unified")
    st.plotly_chart(fig_3, use_container_width=True)

    fig_3a = px.bar(df_3, x="TIMESPAN", y="BURN_TX", color="CHAIN", title="Monthly Tx Count of Liquidity Provider(LP) Burn Actions L1 vs L2", height=500)
    fig_3a.update_layout(hovermode="x unified")
    st.plotly_chart(fig_3a, use_container_width=True)

  with col_4:
    fig_4 = px.histogram(df_3, x="CHAIN", y="LP_REMOVING", color="CHAIN", title="Percent Liquidity Removers L1 vs L2", height=500)
    fig_4.update_layout(hovermode="x unified")
    # fig_4.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_4, use_container_width=True)

    fig_4a = px.histogram(df_3, x="CHAIN", y="BURN_TX", color="CHAIN", title="Percent Tx Count of Liquidity Provider(LP) Burn Actions L1 vs L2", height=500)
    fig_4a.update_layout(hovermode="x unified")
    # fig_4a.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_4a, use_container_width=True)

  


  st.subheader(":red[Grouped by Chains]")
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

  st.markdown("""
  ### FINDINGS 🔎
  The insights drawn from the burning (liquidity removal) section is seen to have similar traits when compared to the mint(liquidity providing), that is:
  - Ethereum dominates in terms of LPs but is behind in terms transaction count.
  - Arbitrum, Polygon and Optimism are the major L2 competitions for Ethereum.
  """)

  


  #Top 100 Liquidity Pools on Uniswap
  st.subheader("Top 100 Liquidity Pools on Uniswap")
  url_4 = "https://api.flipsidecrypto.com/api/v2/queries/8746d30d-cf24-42f3-9479-9414a1aae608/data/latest"
  df_4 = pd.read_json(url_4)
  st.dataframe(df_4, use_container_width=True)

  st.header(":blue[LIQUIDITY PROVIDER CROSSOVERS ACROSS CHAINS]")

  # col_6, col_7, = st.columns(2, gap='large')
  url_6 = "https://api.flipsidecrypto.com/api/v2/queries/fea7ca83-81dd-479c-acd1-23e1fa4c783a/data/latest"
  df_6 = pd.read_json(url_6)

  # url_7 = "https://api.flipsidecrypto.com/api/v2/queries/76e0d726-74a7-47c8-b6c0-54e4503e17f3/data/latest"
  # df_7 = pd.read_json(url_7)

  # with col_6:
  fig_6 = px.bar(df_6, x="CHAIN_CROSSOVER", y="LPS", color="CHAIN_CROSSOVER", title="Monthly Liquidity Removers Across Chains", height=500, log_y=True)
  fig_6.update_layout(hovermode="x unified")
  st.plotly_chart(fig_6, use_container_width=True)

  # with col_7:
  #   st.subheader("Top LPs by Crossovers Across Chains")
  #   st.dataframe(df_7, use_container_width=True)

  st.markdown("""
  FINDINGS 🔎
  Majority of LPs are seen to have provided liquidity on one chain, but crossovers were noticed with about 15 wallets found to have provided liquidity across the seven chains under consideration.

  This is a big rabbit 🐇 hole that cannot be properly exploited in the analysis.
  """)

  
  cola, colb, colc, = st.columns([2,1,2])
  with colb:
    st.image("https://pbs.twimg.com/profile_images/1658503811189850112/yQRHOhdB_400x400.jpg", "Data By: Flipside Crypto", width=200,)

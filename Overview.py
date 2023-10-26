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



  st.header("INTRODUCTION")
  st.markdown("""

In the ever-evolving landscape of decentralized finance (DeFi), Uniswap stands as a pioneer—a beacon of accessibility and innovation that swiftly claimed its throne as the leading Decentralized Exchange (DEX). It all began with a simple yet revolutionary concept: empower both traders and liquidity providers to shape the future of DeFi.

The effectiveness of Uniswap hinges upon a delicate balance, a dance between two equally vital protagonists: the traders executing swaps and the liquidity providers who facilitate these trades. It's a symbiotic relationship that, if disrupted, could send ripples through the DeFi ecosystem.

Imagine a world where liquidity providers vanish; where traders navigate turbulent price seas with no respite in sight. The result? Steep price impacts, a storm of uncertainty, and the traders, the lifeblood of this ecosystem, left gasping for air.

On the flip side, a world without traders would render liquidity providers adrift in stagnant pools, their capital adrift in the vast DeFi sea. The magic of DeFi, where capital begets capital, would be lost, and liquidity providers would face a bleak return on investment.

That's why we've embarked on a journey, a deep dive into the very heart of Uniswap's liquidity providers. We seek to understand who they are, what drives them, and what keeps this DeFi engine running. Through this analytical dashboard, we shall illuminate the enigmatic world of liquidity providers, explore the dominance of the giants and the resilience of the smaller fish, and unveil the intricate dance of liquidity in the Uniswap ocean.

As we journey through this realm, we'll unravel the mysteries of liquidity provider activity and its relation to the size of liquidity provided. We'll examine the consequences of a large liquidity provider leaving a small pool, seeking to discover if others rush to fill the void.

And, as the DeFi space expands, we'll venture into uncharted territories, comparing Ethereum's L1 and the emerging Layer 2 solutions, in pursuit of insights into the shifting tides of liquidity.

This dashboard is not just an analysis; it's a testament to the power of data, a tool to better understand the guardians of liquidity. We invite you to explore, learn, and share, for the strength of DeFi lies in its community. Join us as we navigate the ever-fascinating world of Uniswap liquidity providers.""")

  st.markdown("""
  #### For a more detailed analysis, data for the past month only and all time are presented to help readers explore thier options better.
  ### Charts presented in this section are set to :red[refresh daily.]
  """)


  tab1, tab2 = st.tabs(["Past Month Data",   "All-Time Data"])

  with tab2:
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

  with tab1:
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


  st.markdown("""
  ### FINDINGS
- It was discovered that an impressive sum of 19billion USD has been traded on Uniswap in the past 30 days. A total of approximately 8million transactions with over 1million users interacting with the Uniswap contract in the past Month is an impressive feat to say the least.

- It was also discovered that Ethereum is leading chain in terms of all the presented metrics in both daily and total metrics in the past 30 days with a great margin showing how strong the L1 still is over time in terms of attracting users to engage with the Uniswap contract.

- It was also discovered that a similar trend was seen when observing the all time data presented in the next tab.

- Continue with us as we dig deeper into the analysis by delving into the Liquidity providers activities on Ethereum (more emphasis here) and on Ethereum vs other L2s. To the next tab ➡️
  """)

  cola, colb, colc, = st.columns([2,1,2])
  with colb:
    st.image("https://pbs.twimg.com/profile_images/1658503811189850112/yQRHOhdB_400x400.jpg", "Data By: Flipside Crypto", width=200,)

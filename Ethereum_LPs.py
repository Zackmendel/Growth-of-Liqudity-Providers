import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
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
In this section, we will be monitoring all the activities of Liquidity Providers(LPs) on the Ethereum chain, how they provide liquidity and how they remove them, their distribution against many metrics like their pool type, LP's ETH balance amongst others

We are hoping that at the end of this analysis more insights into the behavior of LPs can be drawn and their behavior can be understood a lot better.
""")

  st.markdown("""
  ### Charts presented in this section are set to :red[refresh daily.]
  """)


  # tab1, tab2 = st.tabs(["All-Time Data", "Past Month Data"])

  # with tab1:
  col0, col1, col3 = st.columns([0.4,2,0.4])
  with col1:
    st.header("1. Top Pools On Uniswap And Their Monthly USD Token Flow")
  col_1, col_2, col_3, col_4 = st.columns(4, gap='large')
  url_0 = "https://api.flipsidecrypto.com/api/v2/queries/81dddab4-3169-4fba-8c83-eb09cf4aa815/data/latest"
  df_0 = pd.read_json(url_0)
  with col_1:
    url_a = "https://api.flipsidecrypto.com/api/v2/queries/3a11d20e-b617-4a37-aa5e-0e2ceb2383b0/data/latest"
    df_a = pd.read_json(url_a)
    st.metric(label="Total Number of Pools", value=(millify(df_a["POOLS"][0], precision=2)))

  with col_2:
    st.metric(label="Total Token Inflow(USD)", value=(millify(df_0["INFLOW"][0], precision=2)))

  with col_3:
    st.metric(label="Total Token Outflow(USD)", value=(millify(df_0["OUTFLOW"][0], precision=2)))

  with col_4:
    st.metric(label="Total Token Netflow(USD)-Balance", value=(millify(df_0["NETFLOW"][0], precision=2)))

  #Monthly Liquidiy Flows
  col_5, col_6 = st.columns([2,1])
  url_3 = "https://api.flipsidecrypto.com/api/v2/queries/e557745a-e989-4c00-84db-fb854d80717f/data/latest"
  df_3 = pd.read_json(url_3)

  with col_5:
    subfig = make_subplots(specs=[[{"secondary_y": True}]])

    # create two independent figures with px.line each containing data from multiple columns
    fig = px.line(df_3, x="TIMESPAN", y=["INFLOW", "OUTFLOW"])
    fig2 = px.line(x=df_3['TIMESPAN'], y=df_3['CUMUL_NETFLOW'])
    # name="CUMUL_NETFLOW", line_color="yellow")

    fig2.update_traces(yaxis="y2")

    subfig.add_traces(fig.data + fig2.data)
    subfig.layout.xaxis.title="Timespan"
    subfig.layout.yaxis.title="Volume"
    # subfig.layout.yaxis2.type="log"
    subfig.layout.yaxis2.title="CUMUL_NETFLOW"
    subfig.update_layout(hovermode="x unified", title="Monthly Inflow & Outflow to Liquidity Pools on Uniswap(USD)", height=500)
    # recoloring is necessary otherwise lines from fig und fig2 would share each color
    # e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this
    subfig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
    st.plotly_chart(subfig, use_container_width=True)


  with col_6:
    fig_3a = px.area(df_3, x="TIMESPAN", y="NETFLOW", title="Monthly Netflows Into Liquidity Pools on Uniswap", height=500)
    fig_3a.update_layout(hovermode="x unified")
    fig_3a.update_traces(line_color='yellow')
    st.plotly_chart(fig_3a, use_container_width=True)

  #Top 100 Liquidity Pools on Uniswap
  st.subheader("Top 100 Liquidity Pools on Uniswap")
  url_4 = "https://api.flipsidecrypto.com/api/v2/queries/38483405-cb4d-4d3a-919e-3eb0446ab258/data/latest"
  df_4 = pd.read_json(url_4)
  st.dataframe(df_4, use_container_width=True)

  cola, colb, colc = st.columns(3, gap="large")

  urla = "https://api.flipsidecrypto.com/api/v2/queries/1ed941c5-e8d6-4ac3-9f01-e7a5f836661d/data/latest"
  dfa = pd.read_json(urla)

  with cola:
    figa = px.bar(dfa, x="POOL_TYPE", y="INFLOW", color="POOL_TYPE", title="Distribution by Pool Type(Inflow)", height=500)
    figa.update_layout(hovermode="x unified")
    st.plotly_chart(figa, use_container_width=True)

  with colb:
    figb = px.bar(dfa, x="POOL_TYPE", y="OUTFLOW", color="POOL_TYPE", title="Distribution by Pool Type(Outflow)", height=500)
    figb.update_layout(hovermode="x unified")
    st.plotly_chart(figb, use_container_width=True)

  with colc:
    figc = px.bar(dfa, x="POOL_TYPE", y="NETFLOW", color="POOL_TYPE", title="Distribution by Pool Type(Netflow)", height=500)
    figc.update_layout(hovermode="x unified")
    st.plotly_chart(figc, use_container_width=True)

  st.markdown("""
### FINDINGS🔎

- A total of about 197thousand liquidity pools have been created on Uniswap all time. A whooping sum of approximately 7billion USD is currently locked in Uniswap pools with over 1.3trillion USD liquidity provided and removed by LPs. This is an impressive feat for Uniswap.

- From the monthly flows of liquidity into Uniswap pools, we can clearly see that LPs add more liquidity to Uniswap than they remove except in rare cases in which June 2023 was the most recent of such cases.

- USDC-USDT on Uniswap V3 which is a stable-stable pool is seen to the top pool of Uniswap on Ethereum with over 475million USD locked in it's contract.

- While comparing the volumes of the different types of pools, we found out that Other pools that has no stables or ETH in them had the highest values in terms of inflow, outflow and netflow(balance).

- Stable-ETH on the other hand can be seen competing with Other pools for amount of Liquidity entering and leaving it, but although still ranking second in terms of the balance left in it, the margin to other pools is seen to be on the high side.
""")


  col0, col1, col3 = st.columns([1,2,1])
  with col1:
    st.header("2. Total and Monthly LP Stats on Uniswap.")
    
  col_7, col_8, = st.columns([2,1])

  with col_7:
    url_7 = "https://api.flipsidecrypto.com/api/v2/queries/74f2537e-396a-4151-a16a-d0854adf9c66/data/latest"
    df_7 = pd.read_json(url_7)

    subfig = make_subplots(specs=[[{"secondary_y": True}]])

    # create two independent figures with px.line each containing data from multiple columns
    fig = px.line(df_7, x="TIMESPAN", y=["LP_ADDING", "LP_REMOVING"])
    fig2 = px.line(x=df_7['TIMESPAN'], y=df_7['CUMUL_LP_ADDING'])
    # name="CUMUL_NETFLOW", line_color="yellow")

    fig2.update_traces(yaxis="y2")

    subfig.add_traces(fig.data + fig2.data)
    subfig.layout.xaxis.title="Timespan"
    subfig.layout.yaxis.title="User Count"
    # subfig.layout.yaxis2.type="log"
    subfig.layout.yaxis2.title="CUMUL_LP_ADDING"
    subfig.update_layout(hovermode="x unified", title="Monthly Liquidity Provider(LP) Actions on Ethereum", height=400)
    # recoloring is necessary otherwise lines from fig und fig2 would share each color
    # e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this
    subfig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
    st.plotly_chart(subfig, use_container_width=True)

    subfig1 = make_subplots(specs=[[{"secondary_y": True}]])

    # create two independent figures with px.line each containing data from multiple columns
    fig = px.line(df_7, x="TIMESPAN", y=["MINT_TX", "BURN_TX"])
    fig2 = px.line(x=df_7['TIMESPAN'], y=df_7['CUMUL_MINT_TX'])
    # name="CUMUL_NETFLOW", line_color="yellow")

    fig2.update_traces(yaxis="y2")

    subfig1.add_traces(fig.data + fig2.data)
    subfig1.layout.xaxis.title="Timespan"
    subfig1.layout.yaxis.title="User Count"
    # subfig.layout.yaxis2.type="log"
    subfig1.layout.yaxis2.title="CUMUL_LP_ADDING"
    subfig1.update_layout(hovermode="x unified", title="Monthly Tx Count of Liquidity Provider(LP) Actions on Ethereum", height=400)
    # recoloring is necessary otherwise lines from fig und fig2 would share each color
    # e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this
    subfig1.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
    st.plotly_chart(subfig1, use_container_width=True)

  with col_8:
    url_8 = "https://api.flipsidecrypto.com/api/v2/queries/9e98609f-21d2-4468-8c46-0655a34cb7cf/data/latest"
    df_8 = pd.read_json(url_8)
    st.metric(label="Total Liquidity Providers Count", value=(millify(df_8["LP_ADDING"][0], precision=2)))
    
    st.metric(label="Total Liquidity Providing Transactions", value=(millify(df_8["MINT_TX"][0], precision=2)))

    url_7 = "https://api.flipsidecrypto.com/api/v2/queries/74f2537e-396a-4151-a16a-d0854adf9c66/data/latest"
    df_7 = pd.read_json(url_7)
    
    fig_3a = px.area(df_7, x="TIMESPAN", y=["NET_MINT_TX", "NET_LP_ADDING"], title="Net LP Mint + Net Tx", height=500)
    fig_3a.update_layout(hovermode="x unified")
    # fig_3a.update_traces(line_color='yellow')
    st.plotly_chart(fig_3a, use_container_width=True)


  st.markdown("""
### FINDINGS🔎
- The growth of Liquidity providing of Uniswap on Ethereum is seen to be rising steadily with time and this can be deduced from the slope of the cumulative curve of the metrics.
- A total of almost 1million liquidity providers has provided liquidity for Uniswap on Ethereum over time with almost 4million liquidity providing transactions.
- Net mint and Net liquidity providing are seen to be on the positive side over time indicating that there were more LPs providing liquidity than those removing liquidity.
""")


  col0, col1, col3 = st.columns([0.7,2,0.7])
  with col1:
    st.header("3. How Long LPs Stay In A Pools on Uniswap.")

  
  st.subheader("Lenght of LPs In Pools")
  # url9 = "https://api.flipsidecrypto.com/api/v2/queries/964833b2-a24e-40bc-b8c5-41147202eeec/data/latest"
  # df9 = pd.read_json(url9)
  # st.dataframe(df9, use_container_width=True)

  col9, col10, = st.columns(2, gap="large")
  with col9:
    
    st.subheader("Top Active LPs by Average Days Spent in Pools")
    
    url9 = "https://api.flipsidecrypto.com/api/v2/queries/4cbb5233-3659-4b54-a371-73d443f6a9af/data/latest"
    df9 = pd.read_json(url9)
    st.dataframe(df9, use_container_width=True)

  with col10:

    st.subheader("Top Pools With Active LPs by Average Days Spent")

    url9 = "https://api.flipsidecrypto.com/api/v2/queries/21eda393-31e5-45fd-951e-6a327e49d22b/data/latest"
    df9 = pd.read_json(url9)
    st.dataframe(df9, use_container_width=True)

  urlx = "https://api.flipsidecrypto.com/api/v2/queries/d50f9537-f94c-4989-9ffc-7f3775c92a21/data/latest"
  dfx = pd.read_json(urlx)

  figx = px.bar(dfx, x="STATS", y="LP_COUNT", color="STATS", title="Distribution of LPs Still Active by Length of Days In Pool", height=500)
  figx.update_layout(hovermode="x unified")
  st.plotly_chart(figx, use_container_width=True)

  st.markdown("""
### FINDINGS🔎
- This section tries to explore the length of active liquidity providers in a pool and it filters out LPs that has their maximum burn(withdrawal) transaction time higher than their maximum mint(liquidity providing) transaction.

- This logic filters out those who removed liquidity after providing it without adding liquidity again.

- And shockingly, there were LPs that has provided liquidity for two years without withdrawal.

- Further research shows that most of the pools that the above mentioned LPs contained only them as the LP at current time indicating low interests in the pools.

- However, an impressive number of LPs have been active for up to a year on Uniswap in Ethereum.
""")


  
    

  col0, col1, col3 = st.columns([1,2,1])
  with col1:
    st.header("4. Distribution of LPs on Uniswap.")
    
  st.subheader("Distribution of LPs Based on ETH Balance")

  col_9, col_10, = st.columns([2,1])
  url_9 = "https://api.flipsidecrypto.com/api/v2/queries/d8368a7f-0f8e-4066-826b-0e43affeec5e/data/latest"
  df_9 = pd.read_json(url_9)

  with col_9:
    fig_9 = px.bar(df_9, x="DISTRIBUTION", y="USERS_COUNT", color="DISTRIBUTION", title="Distribution of LPs Based on ETH Balance", height=500)
    fig_9.update_layout(hovermode="x unified")
    st.plotly_chart(fig_9, use_container_width=True)

  with col_10:
    fig_9a = px.pie(df_9, names="DISTRIBUTION", values="USERS_COUNT", labels="DISTRIBUTION", title="Percent Distribution of LPs Based on ETH Balance", height=500)
    fig_9a.update_layout(hovermode="x unified")
    fig_9a.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_9a, use_container_width=True)

  st.write(":blue[Based on ETH balance], it is discovered that a good amount of LPs are shrimps (<1ETH balance). A good number of whales were also recorded that made about 8.6% of the total LPs.")

  st.subheader("Distribution of LPs by Their Active Months")

  url_10 = "https://api.flipsidecrypto.com/api/v2/queries/5bee15eb-99d3-419d-b373-5ac074e5d1f0/data/latest"
  df_10 = pd.read_json(url_10)
  fig_10 = px.bar(df_10, x="ACTIVITY_OF_LPS", y="LPS", color="ACTIVITY_OF_LPS", title="Active Months of Liquidity Providers", height=500)
  fig_10.update_layout(hovermode="x unified")
  st.plotly_chart(fig_10, use_container_width=True)

  st.markdown("""
  :blue[By their active months] measures the difference between LP's last liquidity provided and current date.
  
  A noticed trend is that inactivity increases with time with most LPs inactive for more than two years now.
  """)
  
  
  st.subheader("Liquidity Providers Distribution Based on UNI Token Holding & Governance")
  
  col_12, col_12a, = st.columns(2, gap="large")
  url_12 = "https://api.flipsidecrypto.com/api/v2/queries/2dd945e1-a063-4990-b55f-be34c99586d3/data/latest"
  df_12 = pd.read_json(url_12)
  
  url_12a = "https://api.flipsidecrypto.com/api/v2/queries/c0c16d0a-5acc-4155-9031-94f5592241e0/data/latest"
  df_12a = pd.read_json(url_12a)
  
  with col_12:
    fig_12 = px.bar(df_12, x="LP_DISTRIBUTION", y="LP_COUNT", color="LP_DISTRIBUTION", title="LP Distribution Based on UNI Token Holding", height=500)
    fig_12.update_layout(hovermode="x unified")
    st.plotly_chart(fig_12, use_container_width=True)
  
  with col_12a:
    fig_12a = px.bar(df_12a, x="LP_DISTRIBUTION", y="LP_COUNT", color="LP_DISTRIBUTION", title="Governance Participation of LPs on Uniswap", height=500)
    fig_12a.update_layout(hovermode="x unified")
    st.plotly_chart(fig_12a, use_container_width=True)
  
  st.markdown(":blue[This section tracks the interest of LPs in Uniswap governance process] and is it can be clearly deduced by the small number of LPs that does not hold the Uniswap native UNI token and the number of LPs that have not participated actively in Uniswap governance that LPs a rarely interested in the governance of Uniswap.")
  
  
  
  st.subheader("Pool Distribution of Uniswap on Ethereum by Pool Balance")
  
  col_11, col_11a, = st.columns(2, gap="large")
  url_11 = "https://api.flipsidecrypto.com/api/v2/queries/4c46147f-2329-48ed-8452-0817d45f3d4a/data/latest"
  df_11 = pd.read_json(url_11)
  
  url_11a = "https://api.flipsidecrypto.com/api/v2/queries/fc66ddc9-2390-4898-ae6e-08678864e6f0/data/latest"
  df_11a = pd.read_json(url_11a)
  
  with col_11:
    fig_11 = px.pie(df_11, names="POOL_DISTRIBUTION", values="POOL_COUNT", color="POOL_DISTRIBUTION", title="Pool Distribution of Uniswap on Ethereum by Pool Balance", height=500)
    fig_11.update_layout(hovermode="x unified")
    fig_11.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_11, use_container_width=True)
  
  with col_11a:
    fig_11a = px.pie(df_11a, names="POOL_DISTRIBUTION", values="LP_COUNT", labels="POOL_DISTRIBUTION", title="User Count of Pool Distribution by Pool Balance", height=500)
    fig_11a.update_layout(hovermode="x unified")
    fig_11a.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_11a, use_container_width=True)
  
  st.markdown("""
  - By pool balance, Liquidity pools with balance >=1000000 is considered large, balance < 1000000 and > 100000 is considered medium and balance < 100000 are considered small pools.
  
  - A very large number of pools fell in the Medium size category, followed by Small size pools and with a very minute 3.3% falling into the Large pools category.
  
  - Interestingly, there were a lot of LPs concentrated in the large pools(44.2%) and a very small amount of LPs(6.7%) in the small pool and as usual the Medium pool still has a higher number of LPs.
  """)
  
  col0, col1, col3 = st.columns([1,2,1])
  with col1:
    st.header("5. Heatmap of Uniswap LPs Actions.")
  
  url_00 = "https://api.flipsidecrypto.com/api/v2/queries/bb749b5e-d4f0-43bc-a53e-3e8c5efd58c3/data/latest"
  df_00 = pd.read_json(url_00)
  
  fig_00 = px.scatter(df_00, x="MONTHS", y="DAYS", color="DAYS",
     size='LP_ADDING', hover_data=['LP_ADDING'], title="Monthly Liquidity Provider(LP) Actions Heatmap", height=500)
  st.plotly_chart(fig_00, use_container_width=True)
  
  
  
  col_13, col_13a, = st.columns(2, gap="large")
  url_13 = "https://api.flipsidecrypto.com/api/v2/queries/bb749b5e-d4f0-43bc-a53e-3e8c5efd58c3/data/latest"
  df_13 = pd.read_json(url_13)
  
  with col_13:
    fig_13 = px.histogram(df_13, x="HOURS", y=["MINT_TX", "LP_ADDING"], barmode='group', title="Active Hours of LPs on Uniswap", height=500)
    fig_13.update_layout(hovermode="x unified")
    st.plotly_chart(fig_13, use_container_width=True)
  
  with col_13a:
    fig_13a = px.histogram(df_13, x="DAYS", y=["MINT_TX", "LP_ADDING"], barmode='group', title="Active days of LPs on Uniswap", height=500)
    fig_13a.update_layout(hovermode="x unified")
    st.plotly_chart(fig_13a, use_container_width=True)
  
  st.markdown("""
  - September can be seen to ve the most active month all time for Liquidity providers of Uniswap on Ethereum. Tuesday - Thursday are also seen to be the most active days in that month of September.
  
  - Liquidity providers are more active during the late hours and very early hours of the day 
  """)

  # with col_10:
  #   fig_1a = px.bar(df_1, x="BLOCKCHAIN", y="SWAP_COUNT", color="BLOCKCHAIN", title="Uniswap Swap Count", height=400)
  #   fig_1a.update_layout(hovermode="x unified")
  #   st.plotly_chart(fig_1a, use_container_width=True)

  #   fig_2a = px.bar(df_2, x="TIMESPAN", y="SWAP_COUNT", color="BLOCKCHAIN", title="Uniswap Monthly Swap Count", height=400)
  #   fig_2a.update_layout(hovermode="x unified")
  #   st.plotly_chart(fig_2a, use_container_width=True)

  # with col_3:
  #   fig_1b = px.bar(df_1, x="BLOCKCHAIN", y="USERS_COUNT", color="BLOCKCHAIN", title="Uniswap Swappers Count", height=400)
  #   fig_1b.update_layout(hovermode="x unified")
  #   st.plotly_chart(fig_1b, use_container_width=True)

  #   fig_2b = px.bar(df_2, x="TIMESPAN", y="USERS_COUNT", color="BLOCKCHAIN", title="Uniswap Monthly Swappers Count", height=400)
  #   fig_2b.update_layout(hovermode="x unified")
  #   st.plotly_chart(fig_2b, use_container_width=True)

  # with tab2:
  #   st.header("Past Month Trading Stats on Uniswap")
  #   col_1, col_2, col_3 = st.columns(3, gap='large')
  #   url_0 = "https://api.flipsidecrypto.com/api/v2/queries/049c7e47-b730-44aa-9ee3-1dfd70550950/data/latest"
  #   df_0 = pd.read_json(url_0)
  #   with col_1:
  #     st.metric(label="Total Volume Traded on Uniswap(Past Month)", value=(millify(df_0["VOLUME_USD"][0], precision=2)))

  #   with col_2:
  #     st.metric(label="Total Swap Count on Uniswap(Past Month)", value=(millify(df_0["SWAP_COUNT"][0], precision=2)))

  #   with col_3:
  #     st.metric(label="Total User Count on Uniswap(Past Month)", value=(millify(df_0["USERS_COUNT"][0], precision=2)))


  #   col_1, col_2, col_3 = st.columns(3, gap='large')
  #   url_1 = "https://api.flipsidecrypto.com/api/v2/queries/fd826701-a84e-4a6e-bd66-d6fc16eb7f3c/data/latest"
  #   df_1 = pd.read_json(url_1)

  #   url_2 = "https://api.flipsidecrypto.com/api/v2/queries/1d5d5dec-2632-4055-887d-dea097b301e9/data/latest"
  #   df_2 = pd.read_json(url_2)

  #   with col_1:
  #     fig_1 = px.bar(df_1, x="BLOCKCHAIN", y="VOLUME_USD", color="BLOCKCHAIN", title="Uniswap Trading Volume(Past Month)", height=400)
  #     fig_1.update_layout(hovermode="x unified")
  #     st.plotly_chart(fig_1, use_container_width=True)

  #     fig_2 = px.bar(df_2, x="TIMESPAN", y="VOLUME_USD", color="BLOCKCHAIN", title="Uniswap Daily Trading Volume(Past Month)", height=400)
  #     fig_2.update_layout(hovermode="x unified")
  #     st.plotly_chart(fig_2, use_container_width=True)

  #   with col_2:
  #     fig_1a = px.bar(df_1, x="BLOCKCHAIN", y="SWAP_COUNT", color="BLOCKCHAIN", title="Uniswap Swap Count(Past Month)", height=400)
  #     fig_1a.update_layout(hovermode="x unified")
  #     st.plotly_chart(fig_1a, use_container_width=True)

  #     fig_2a = px.bar(df_2, x="TIMESPAN", y="SWAP_COUNT", color="BLOCKCHAIN", title="Uniswap Daily Swap Count(Past Month)", height=400)
  #     fig_2a.update_layout(hovermode="x unified")
  #     st.plotly_chart(fig_2a, use_container_width=True)

  #   with col_3:
  #     fig_1b = px.bar(df_1, x="BLOCKCHAIN", y="USERS_COUNT", color="BLOCKCHAIN", title="Uniswap Swappers Count(Past Month)", height=400)
  #     fig_1b.update_layout(hovermode="x unified")
  #     st.plotly_chart(fig_1b, use_container_width=True)

  #     fig_2b = px.bar(df_2, x="TIMESPAN", y="USERS_COUNT", color="BLOCKCHAIN", title="Uniswap Daily Swappers Count(Past Month)", height=400)
  #     fig_2b.update_layout(hovermode="x unified")
  #     st.plotly_chart(fig_2b, use_container_width=True)

  cola, colb, colc, = st.columns([2,1,2])
  with colb:
    st.image("https://pbs.twimg.com/profile_images/1658503811189850112/yQRHOhdB_400x400.jpg", "Data By: Flipside Crypto", width=200,)

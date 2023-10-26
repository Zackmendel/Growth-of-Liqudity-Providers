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

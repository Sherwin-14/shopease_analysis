# utils.py
import os  
import numpy as np
import pandas as pd
import streamlit as st
import dask.dataframe as dd
import polars as pl
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import streamlit_shadcn_ui as ui
import warnings
warnings.filterwarnings("ignore")




from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabasz_score
from line_profiler import profile
from wordcloud import WordCloud
from pandas.api.types import CategoricalDtype


# Set permanent wide mode
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

df_data_intro = dd.read_csv('data/cleaned_dataset.csv',header=0,engine='python')
df_rfm = dd.read_csv('data/rfm_df.csv',header=0,engine='python')
df_transformed = dd.read_parquet('data/transformed_dataset.parquet')






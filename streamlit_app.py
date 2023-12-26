import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import sqlite3


st.title("Recall Analysis")

def get_data_from_DB() -> pd.DataFrame:
  con = sqlite3.connect('recall.db')
  df = pd.read_sql_query("SELECT * FROM tb_recalls", con)
  con.close()
  return df

df = get_data_from_DB()
st.dataframe(df)

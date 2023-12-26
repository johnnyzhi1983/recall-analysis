import pandas as pd
import streamlit as st
import sqlite3
st.set_page_config(page_title='RecallAnalysis', layout='wide')
import openai
from pandasai import SmartDataframe
from pandasai.llm import OpenAI


st.title("Recall Analysis")

llm = OpenAI(api_token=st.secrets["openAI_SK"])

def get_data_from_DB() -> pd.DataFrame:
  con = sqlite3.connect('recall.db')
  df = pd.read_sql_query("SELECT url, title, date, content FROM tb_recalls", con)
  con.close()
  return df


if __name__ == '__main__':
  recall_exp = st.expander("Click to see the raw data...", expanded=False)
  df = get_data_from_DB()
  with recall_exp:    
    st.dataframe(df)
  sdf = SmartDataframe(df, config={"llm": llm})
  st.write(sdf.chat('How many recall cases happened in December 2023?'))

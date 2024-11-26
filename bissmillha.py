# example/st_app_gsheets_using_service_account.py
import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Read Google Sheet as DataFrame")
conn = st.connection("gsheets", type=GSheetsConnection)
#df = conn.read(worksheet = "Sheet1" , usecols = list(range(6), ttl = 5))
#df = conn.read(worksheet = “Sheet1” , usecols= list(range(6)), ttl = 5)
#data = conn.read(spreadsheet=url, usecols=[0, 3])
#st.write(st.secrets['connections']) 
df = conn.read(worksheet="Sheet1")
st.dataframe(df)
with st.form(key="muhammad"):
    company = st.text_input(label="stdnamee")
    submit_button =  st.form_submit_button(label="submit the data")
    if submit_button:
    #df["stname"].str.contains(company).any():
        vendor_data = pd.DataFrame([{"name":company}])
        update_df =   pd.concat([df , vendor_data] , ignore_index=True)
        conn.update(worksheet="Sheet1", data=update_df)
     #   st.dataframe(vendor_data)
        

        st.title("ok ok ok ok ")
      #  st.dataframe(df)


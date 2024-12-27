from openpyxl import Workbook
import streamlit as st  
import pandas as pd
#url = "https://docs.google.com/spreadsheets/d/1-6-dNTXR3YLAvRIDRWf9DQsdXw3EAJWt/edit?usp=sharing&ouid=105182257404870437876&rtpof=true&sd=true"
url = "https://docs.google.com/spreadsheets/d/1-6-dNTXR3YLAvRIDRWf9DQsdXw3EAJWt/edit?usp=sharing&ouid=105182257404870437876&rtpof=true&sd=true"
file_id = url.split("/")[-2]
path1 = "https://drive.google.com/uc?export=download&id=" + file_id
sce = pd.read_excel(path1)
st.write(sce)



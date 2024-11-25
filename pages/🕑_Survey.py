import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import json

# Google Sheets setup
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Load credentials from Streamlit Secrets
creds_json = json.loads(st.secrets["GOOGLE_APPLICATION_CREDENTIALS_JSON"])
creds = Credentials.from_service_account_info(creds_json, scopes=scope)

# Authenticate with Google Sheets
client = gspread.authorize(creds)
sheet = client.open('Survey Results').sheet1  

def store_survey_response(color, beverage, work_pref, environment):
    sheet.append_row([color, beverage, work_pref, environment])

def get_survey_data():
    # Get all the data in the sheet
    data = sheet.get_all_records()
    return pd.DataFrame(data)

# Define the app structure with tabs
tab1, tab2, tab3, tab4 = st.tabs(["Survey 1", "Survey 2", "Results 1", "Results 2"])

with tab1:
    st.header("Survey 1 - Multiple Choice Questions")
    q1 = st.radio("What is your favorite color?", ["Blue", "Green", "Red"])
    q2 = st.radio("Coffee or Tea?", ["Coffee", "Tea"])
    q3 = st.radio("Do you prefer working from home?", ["Yes", "No"])
    if st.button("Submit Survey 1"):
        store_survey_response(q1, q2, q3, None)
        st.success("Survey 1 submitted successfully!")

with tab2:
    st.header("Survey 2 - Text Input")
    text_response = st.text_area("Describe your ideal work environment:")
    if st.button("Submit Survey 2"):
        store_survey_response(None, None, None, text_response)
        st.success("Survey 2 submitted successfully!")

with tab3:
    st.header("Results of Survey 1")
    data = get_survey_data()
    if not data.empty:
        fig, axs = plt.subplots(3, 1, figsize=(8, 12))
        sns.countplot(data=data, x='Color', ax=axs[0], palette='viridis')
        axs[0].set_title("Favorite Colors")
        sns.countplot(data=data, x='Beverage', ax=axs[1], palette='Set2')
        axs[1].set_title("Coffee or Tea")
        sns.countplot(data=data, x='WorkPreference', ax=axs[2], palette='Set1')
        axs[2].set_title("Work From Home Preference")
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.write("No responses yet.")

with tab4:
    st.header("Word Cloud from Survey 2 Responses")
    data = get_survey_data()
    if not data.empty and 'Environment' in data.columns and data['Environment'].notna().any():
        from wordcloud import WordCloud
        combined_text = " ".join(data['Environment'].dropna())
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(combined_text)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.write("No text responses yet.")

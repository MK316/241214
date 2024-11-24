import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select
import pandas as pd

# Initialize the database connection
engine = create_engine('sqlite:///survey_data.db')
metadata = MetaData()
surveys = Table('surveys', metadata,
                Column('id', Integer, primary_key=True),
                Column('color', String),
                Column('beverage', String),
                Column('work_preference', String),
                Column('environment', String))

metadata.create_all(engine)  # Create the tables if they don't already exist

def store_survey_responses(color, beverage, work_pref, environment):
    with engine.connect() as connection:
        ins = surveys.insert().values(color=color, beverage=beverage, work_preference=work_pref, environment=environment)
        connection.execute(ins)

def get_survey_data():
    with engine.connect() as connection:
        query = select([surveys])
        result = pd.read_sql(query, connection)
    return result

# Define the app structure with tabs
tab1, tab2, tab3, tab4 = st.tabs(["Survey 1", "Survey 2", "Results 1", "Results 2"])

with tab1:
    st.header("Survey 1 - Multiple Choice Questions")
    q1 = st.radio("What is your favorite color?", ("Blue", "Green", "Red"))
    q2 = st.radio("Coffee or Tea?", ("Coffee", "Tea"))
    q3 = st.radio("Do you prefer working from home?", ("Yes", "No"))
    if st.button("Submit Survey 1"):
        store_survey_responses(q1, q2, q3, None)
        st.success("Survey 1 submitted successfully!")

with tab2:
    st.header("Survey 2 - Text Input")
    text_response = st.text_area("Describe your ideal work environment:")
    if st.button("Submit Survey 2"):
        store_survey_responses(None, None, None, text_response)
        st.success("Survey 2 submitted successfully!")

with tab3:
    st.header("Results of Survey 1")
    data = get_survey_data()
    if not data.empty and 'color' in data.columns and data['color'].notna().any():
        fig, axs = plt.subplots(3, 1, figsize=(8, 12))
        sns.countplot(data=data, x='color', ax=axs[0], palette='viridis')
        axs[0].set_title("Favorite Colors")
        sns.countplot(data=data, x='beverage', ax=axs[1], palette='Set2')
        axs[1].set_title("Coffee or Tea")
        sns.countplot(data=data, x='work_preference', ax=axs[2], palette='Set1')
        axs[2].set_title("Work From Home Preference")
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.write("No responses yet.")

with tab4:
    st.header("Word Cloud from Survey 2 Responses")
    data = get_survey_data()
    if not data.empty and 'environment' in data.columns and data['environment'].notna().any():
        from wordcloud import WordCloud
        combined_text = " ".join(data['environment'].dropna())
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(combined_text)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.write("No text responses yet.")

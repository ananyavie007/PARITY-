import streamlit as st
import pandas as pd

# Load and clean data
df = pd.read_csv("2025-grievances.csv")
df.rename(columns={
    "Ward Name": "Ward",
    "issue_type": "Category",
    "complaint_text": "Complaint",
    "Grievance Date": "Date"
}, inplace=True)
df = df.drop_duplicates()
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Quarter'] = df['Date'].dt.to_period('Q')

# Dashboard title
st.title("PARITY – Citizen Voice Dashboard")

# Section 1: Complaints by Category
st.subheader("Complaints by Category")
st.bar_chart(df['Category'].value_counts())

# Section 2: Top 10 Wards
st.subheader("Top 10 Wards by Complaints")
st.bar_chart(df['Ward'].value_counts().head(10))

# Section 3: Complaints per Quarter by Category
st.subheader("Complaints per Quarter by Category")
quarter_counts = df.groupby(['Quarter','Category']).size().reset_index(name='Counts')
st.dataframe(quarter_counts.head(20))

# Section 4: Filter by Ward
st.subheader("Filter Complaints by Ward")
ward_choice = st.selectbox("Choose a Ward:", df['Ward'].unique())
filtered = df[df['Ward'] == ward_choice]
st.write(filtered[['Date','Category','Complaint ID']].head(10))

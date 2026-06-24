import pandas as pd

# Load the CSV file
df = pd.read_csv("2025-grievances.csv")

# Preview first 5 rows
print(df.head())
# Rename columns for clarity
df.rename(columns={
    "Ward Name": "Ward",
    "issue_type": "Category",
    "complaint_text": "Complaint",
    "Grievance Date": "Date"
}, inplace=True)

# Drop duplicates
df = df.drop_duplicates()
# Display as a nice table
from IPython.display import display
display(df.head(10))
df.to_csv("clean_grievances.csv", index=False)
# Load the CSV file
df = pd.read_csv("2025-grievances.csv")

# Rename columns for clarity
df.rename(columns={
    "Ward Name": "Ward",
    "issue_type": "Category",
    "complaint_text": "Complaint",
    "Grievance Date": "Date"
}, inplace=True)

# Drop duplicates
df = df.drop_duplicates()

df['Ward'].value_counts()
df['Category'].value_counts()
#grouping the wards and getting top 10 probs using desc
df.groupby("Ward").size().sort_values(ascending=False).head(10)
#showing probs per quater
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df['Quarter'] = df['Date'].dt.to_period('Q')
df.groupby(['Quarter','Category']).size().sort_values(ascending=False).head(10)
import matplotlib.pyplot as plt
import seaborn as sns

# Complaints per Category
plt.figure(figsize=(8,5))
sns.countplot(x="Category", data=df, order=df['Category'].value_counts().index)
plt.title("Complaints by Category")
plt.xticks(rotation=90)
plt.show()

# making heatmap ward wise
ward_counts = df['Ward'].value_counts().reset_index()
ward_counts.columns = ['Ward','Complaints']

plt.figure(figsize=(12,6))
sns.barplot(x='Ward', y='Complaints', data=ward_counts.head(15))
plt.xticks(rotation=90)
plt.title("Top 15 Wards by Complaints")
plt.show()


# Complaints per Quarter
quarter_counts = df.groupby(['Quarter','Category']).size().reset_index(name='Counts')
plt.figure(figsize=(12,6))
sns.barplot(x="Quarter", y="Counts", hue="Category", data=quarter_counts)
plt.title("Complaints per Quarter by Category")
plt.xticks(rotation=90)
plt.show()

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

st.title("PARITY – Citizen Voice Dashboard")

# Complaints by Category
st.subheader("Complaints by Category")
st.bar_chart(df['Category'].value_counts())

# Top 10 Wards
st.subheader("Top 10 Wards by Complaints")
st.bar_chart(df['Ward'].value_counts().head(10))

# Complaints per Quarter
st.subheader("Complaints per Quarter by Category")
quarter_counts = df.groupby(['Quarter','Category']).size().reset_index(name='Counts')
st.dataframe(quarter_counts.head(10))
import streamlit as st
st.title("Hello, Streamlit!")

print(df.columns)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import wordcloud as wordcloud_

# Load and clean data
df = pd.read_csv("2025-grievances.csv")

df.rename(columns={
    "Complaint ID": "Complaint",
    "Category": "Category",
    "Sub Category": "Subcategory",
    "Grievance Date": "Date",
    "Ward Name": "Ward",
    "Grievance Status": "Status",
    "Staff Remarks": "Remarks",
    "Staff Name": "Staff"
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
st.write(filtered[['Date','Category','Complaint']].head(10))

text = " ".join(filtered['Remarks'].dropna().astype(str))

if text.strip():
    wc = wordcloud_.WordCloud(width=800, height=400, background_color="black").generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
else:
    st.warning("No staff remarks available for this ward.")
st.download_button("Download Complaints", df.to_csv().encode('utf-8'), "complaints.csv", "text/csv")


#LEADER BY WARD
st.subheader("🏆 Complaint Leaderboard by Ward")

# Count complaints per ward
leaderboard = df['Ward'].value_counts().reset_index()
leaderboard.columns = ['Ward', 'Total Complaints']

# Show as a table
st.write(leaderboard)

# Or highlight top 5 wards
st.write("Top 5 Wards with Most Complaints:")
st.write(leaderboard.head(5))

#BY CATEGORY
st.subheader("📌 Complaint Leaderboard by Category")

category_leaderboard = df['Category'].value_counts().reset_index()
category_leaderboard.columns = ['Category', 'Total Complaints']

st.write(category_leaderboard)





st.metric("🥇 Top Ward", leaderboard.iloc[0]['Ward'], leaderboard.iloc[0]['Total Complaints'])
st.metric("🥈 Second", leaderboard.iloc[1]['Ward'], leaderboard.iloc[1]['Total Complaints'])
st.metric("🥉 Third", leaderboard.iloc[2]['Ward'], leaderboard.iloc[2]['Total Complaints'])

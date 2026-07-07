“Parity: Citizen Grievance Dashboard”  
(Parity = fairness, balance, and equal voice)

  PROBLEM STATEMENT-
  “Citizens raise thousands of grievances every year, but these complaints often remain buried in spreadsheets. Decision‑makers struggle to identify patterns, prioritize issues, and respond effectively.”

  SOLUTION-
  “Our dashboard transforms raw grievance data into clear, interactive insights. Leaders can now see which wards face the most issues, track complaint trends over time, and visualize citizen voices through word clouds and leaderboards.”

TOOLS USED-
Python (data processing)
Pandas (data cleaning & analysis)
Streamlit (dashboard UI)
Matplotlib / Plotly (charts & graphs)
WordCloud (citizen voice visualization)

FEATURES-
📊 KPIs: Total complaints, wards covered, categories.
🏆 Leaderboard: Top wards/categories with most complaints.
📈 Trend Analysis: Complaints over time.
🌍 Filters: Ward, category, date range.
🗣️ Word Cloud: Citizen voice visualization.
📥 Download Option: Export filtered complaints as CSV.
💡 Sentiment Analysis (optional): Positive vs negative complaints.

Instructions to Run
Install dependencies:

bash
pip install streamlit pandas matplotlib wordcloud plotly
Place your CSV file (2025-grievances.csv) in the project folder.

Run the dashboard:

bash
streamlit run parity_dashboard.py
Open the link in your browser (usually http://localhost:8501).

Interact with filters, charts, and word cloud.



# -*- coding: utf-8 -*-
"""country_wise_latest.csv

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z_H8Fy46AO-sremBmTPhJQ1q98I-DyRD

# 🌍 COVID-19 Global Data Analysis Dashboard

This project analyzes global COVID-19 trends using the **latest country-wise dataset** from Kaggle.  
We explore:

- 🌐 Top 10 affected countries
- ⚰️ Case Fatality Rates (CFR)
- ✅ Recovery Rates
- 📊 Data visualized with Matplotlib & Seaborn

---
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
plt.style.use('seaborn-whitegrid')

"""## 📂 Step 1: Upload and Load the Dataset

We use the `country_wise_latest.csv` file from Kaggle (COVID-19 dataset).

"""

from google.colab import files
uploaded = files.upload()

df = pd.read_csv("country_wise_latest.csv")
df.head()

"""## 🧹 Step 2: Clean & Filter Important Columns
We'll keep only the relevant columns: Confirmed, Deaths, Recovered, Active.

"""

df = df[['Country/Region', 'Confirmed', 'Deaths', 'Recovered', 'Active']].dropna()
df.head()

"""## 🌐 Step 3: Top 10 Countries by Confirmed Cases
Visualizing countries with the highest total confirmed cases.

"""

top_confirmed = df.sort_values(by='Confirmed', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_confirmed['Confirmed'], y=top_confirmed['Country/Region'], palette='Reds_r')
plt.title("Top 10 Countries by Confirmed COVID-19 Cases")
plt.xlabel("Confirmed Cases")
plt.ylabel("Country")
plt.show()

"""## ⚰️ Step 4: Case Fatality Rate (CFR)
CFR is calculated as:  
**CFR = (Deaths / Confirmed Cases) × 100**

"""

df['CFR'] = (df['Deaths'] / df['Confirmed']) * 100
top_cfr = df[df['Confirmed'] > 1000].sort_values('CFR', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_cfr['CFR'], y=top_cfr['Country/Region'], palette='magma')
plt.title("Top 10 Countries by Case Fatality Rate")
plt.xlabel("CFR (%)")
plt.ylabel("Country")
plt.show()

"""## ✅ Step 5: Recovery Rate by Country
Calculated as:  
**Recovery Rate = (Recovered / Confirmed Cases) × 100**

"""

df['RecoveryRate'] = (df['Recovered'] / df['Confirmed']) * 100
top_recovery = df[df['Confirmed'] > 1000].sort_values('RecoveryRate', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_recovery['RecoveryRate'], y=top_recovery['Country/Region'], palette='Greens')
plt.title("Top 10 Countries by Recovery Rate")
plt.xlabel("Recovery Rate (%)")
plt.ylabel("Country")
plt.show()

"""## 📈 Conclusion

This dashboard gave a quick overview of the **COVID-19 global situation**, based on the latest confirmed, recovered, and death figures by country.

We visualized:
- Top 10 most affected countries
- Countries with the highest CFR
- Recovery rate leaders

📊 Built using Python, Pandas, and Seaborn in Google Colab.

"""
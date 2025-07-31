import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import streamlit as st

# Giả sử df đã được load sẵn từ load_data() hoặc trực tiếp
# Nếu chưa load, bạn có thể load trong đây:

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/DuyLinh-Data/DA_self_learning/main/Stats_covid19/data/covid_grouped.csv"
    df = pd.read_csv(url)
    df['date'] = pd.to_datetime(df['date'])  # chuyển cột date sang datetime
    return df

df = load_data()

# --- Chart 1: Daily statistics ---
df_daily = df.groupby('date')[['confirmed', 'deaths', 'recovered']].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(df_daily['date'], df_daily['confirmed'], label='Confirmed', color='blue')
plt.plot(df_daily['date'], df_daily['deaths'], label='Deaths', color='red')
plt.plot(df_daily['date'], df_daily['recovered'], label='Recovered', color='green')
plt.title('COVID-19 Cases by Day')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)  # Hiển thị trong Streamlit
plt.clf()       # Xóa figure để tránh chồng chéo

# --- Chart 2: Monthly-Yearly statistics ---
df['month_year'] = df['date'].dt.to_period('M')
df_monthly = df.groupby('month_year')[['confirmed', 'deaths', 'recovered']].sum().reset_index()
df_monthly['month_year'] = df_monthly['month_year'].astype(str)

plt.figure(figsize=(12, 6))
plt.plot(df_monthly['month_year'], df_monthly['confirmed'], label='Confirmed', color='blue', marker='o')
plt.plot(df_monthly['month_year'], df_monthly['deaths'], label='Deaths', color='red', marker='o')
plt.plot(df_monthly['month_year'], df_monthly['recovered'], label='Recovered', color='green', marker='o')
plt.title('COVID-19 Cases by Month')
plt.xlabel('Month-Year')
plt.ylabel('Number of Cases')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Tắt scientific notation trên trục y
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,}'))

st.pyplot(plt)
plt.clf()

# --- Identify the peak day ---
peak_confirmed = df_daily.loc[df_daily['confirmed'].idxmax()]
peak_deaths = df_daily.loc[df_daily['deaths'].idxmax()]
peak_recovered = df_daily.loc[df_daily['recovered'].idxmax()]

st.write(f"📈 Peak Confirmed: {peak_confirmed['date'].date()} with {peak_confirmed['confirmed']:,} cases")
st.write(f"💀 Peak Deaths: {peak_deaths['date'].date()} with {peak_deaths['deaths']:,} deaths")
st.write(f"💚 Peak Recovered: {peak_recovered['date'].date()} with {peak_recovered['recovered']:,} recoveries")

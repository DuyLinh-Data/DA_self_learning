import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# --- Load dữ liệu từ GitHub và xử lý ---
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/DuyLinh-Data/DA_self_learning/main/Stats_covid19/data/covid_grouped.csv"
    df = pd.read_csv(url)

    # Làm sạch tên cột: bỏ khoảng trắng, đưa về chữ thường
    df.columns = df.columns.str.strip().str.lower()

    # Kiểm tra cột 'date' có tồn tại không
    if 'date' not in df.columns:
        st.error("❌ Không tìm thấy cột 'date' trong dữ liệu. Kiểm tra lại tên cột trong file CSV.")
        return pd.DataFrame()

    # Chuyển cột 'date' sang kiểu datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    return df

# --- Load dữ liệu ---
df = load_data()

# --- Kiểm tra dữ liệu trước khi vẽ ---
if not df.empty:
    st.title("📊 Phân tích dữ liệu COVID-19 toàn cầu")

    # --- Biểu đồ theo ngày ---
    df_daily = df.groupby('date')[['confirmed', 'deaths', 'recovered']].sum().reset_index()

    st.subheader("1. Biểu đồ theo ngày")
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
    st.pyplot(plt)
    plt.clf()

    # --- Biểu đồ theo tháng ---
    st.subheader("2. Biểu đồ theo tháng")
    df['month_year'] = df['date'].dt.to_period('M').astype(str)
    df_monthly = df.groupby('month_year')[['confirmed', 'deaths', 'recovered']].sum().reset_index()

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
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
    st.pyplot(plt)
    plt.clf()

    # --- Ngày đạt đỉnh ---
    st.subheader("3. 📍 Ngày đạt đỉnh")
    peak_confirmed = df_daily.loc[df_daily['confirmed'].idxmax()]
    peak_deaths = df_daily.loc[df_daily['deaths'].idxmax()]
    peak_recovered = df_daily.loc[df_daily['recovered'].idxmax()]

    st.markdown(f"📈 **Peak Confirmed:** {peak_confirmed['date'].date()} — {peak_confirmed['confirmed']:,} cases")
    st.markdown(f"💀 **Peak Deaths:** {peak_deaths['date'].date()} — {peak_deaths['deaths']:,} deaths")
    st.markdown(f"💚 **Peak Recovered:** {peak_recovered['date'].date()} — {peak_recovered['recovered']:,} recoveries")
else:
    st.warning("Không có dữ liệu để hiển thị.")

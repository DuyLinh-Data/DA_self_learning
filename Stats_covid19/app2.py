import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("🌍 COVID-19 Pandemic Statistics Dashboard")
st.markdown("Hiển thị dữ liệu theo vùng địa lý WHO. Dữ liệu lấy từ WHO - cập nhật từ GitHub.")

# Đọc dữ liệu từ GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/DuyLinh-Data/DA_self_learning/main/Stats_covid19/data/covid_grouped.csv"
    df = pd.read_csv(url, parse_dates=["date"])
    return df

df = load_data()

# Sidebar: Chọn vùng WHO
regions = sorted(df["WHO Region"].dropna().unique())
selected_regions = st.sidebar.multiselect("🌐 Chọn vùng WHO:", regions, default=regions)

# Lọc theo vùng
df_filtered = df[df["WHO Region"].isin(selected_regions)]

# Sidebar: Chọn ngày và thời gian
min_date = df_filtered["date"].min().date()
max_date = df_filtered["date"].max().date()
start_date = st.sidebar.date_input("📅 Ngày bắt đầu:", min_value=min_date, max_value=max_date, value=min_date)
end_date = st.sidebar.date_input("📅 Ngày kết thúc:", min_value=min_date, max_value=max_date, value=max_date)

# Xử lý ngày
df_filtered = df_filtered[
    (df_filtered["date"].dt.date >= start_date) & 
    (df_filtered["date"].dt.date <= end_date)
]

# Tùy chọn hiển thị dạng biểu đồ
metric = st.radio("📊 Chọn loại dữ liệu:", ("Confirmed", "Recovered", "Deaths"))

# Tổng hợp dữ liệu
df_grouped = df_filtered.groupby(["date", "WHO Region"])[metric].sum().reset_index()

# Vẽ biểu đồ
fig = px.line(
    df_grouped,
    x="date",
    y=metric,
    color="WHO Region",
    title=f"{metric} cases by WHO Region over Time",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

# Hiển thị dữ liệu gốc nếu muốn
if st.checkbox("📄 Hiển thị bảng dữ liệu gốc"):
    st.dataframe(df_filtered)

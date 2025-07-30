import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")
st.title("🦠 Phân tích COVID-19 theo thời gian và địa lý")

# Tải dữ liệu (dùng link raw hoặc file nội bộ nếu có)
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/DuyLinh-Data/DA_self_learning/main/Stats_covid19/world_covid19_data.csv"
    df = pd.read_csv(url)
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

# Kiểm tra cột dữ liệu có đúng không
expected_cols = ['country_region', 'date', 'confirmed', 'recovered', 'deaths']
if not all(col in df.columns for col in expected_cols):
    st.error("⚠️ File dữ liệu không đúng định dạng. Cần các cột: " + ", ".join(expected_cols))
    st.stop()

# Bộ lọc
with st.sidebar:
    st.header("🔍 Bộ lọc")
    countries = st.multiselect("Chọn quốc gia", options=df['country_region'].unique(), default=['Vietnam', 'United States'])
    date_range = st.date_input("Chọn khoảng thời gian", [df['date'].min(), df['date'].max()])

# Lọc dữ liệu
filtered_df = df[
    (df['country_region'].isin(countries)) &
    (df['date'] >= pd.to_datetime(date_range[0])) &
    (df['date'] <= pd.to_datetime(date_range[1]))
]

# Hiển thị tổng số liệu
st.subheader("📈 Tổng số ca (từ dữ liệu đã lọc)")
col1, col2, col3 = st.columns(3)
col1.metric("🦠 Ca nhiễm", f"{filtered_df['confirmed'].sum():,}")
col2.metric("💪 Hồi phục", f"{filtered_df['recovered'].sum():,}")
col3.metric("☠️ Tử vong", f"{filtered_df['deaths'].sum():,}")

# Biểu đồ theo thời gian
st.subheader("📅 Diễn biến theo thời gian")
fig = px.line(
    filtered_df,
    x="date",
    y=["confirmed", "recovered", "deaths"],
    color_discrete_map={"confirmed": "orange", "recovered": "green", "deaths": "red"},
    labels={"value": "Số ca", "variable": "Loại", "date": "Ngày"},
    title="Tình hình COVID-19 theo thời gian"
)
st.plotly_chart(fig, use_container_width=True)

# Biểu đồ theo quốc gia
st.subheader("🌍 Tổng số ca theo quốc gia")
agg = filtered_df.groupby("country_region")[["confirmed", "recovered", "deaths"]].sum().reset_index()

fig2 = px.bar(
    agg.melt(id_vars="country_region", value_vars=["confirmed", "recovered", "deaths"]),
    x="value",
    y="country_region",
    color="variable",
    orientation="h",
    title="Tổng số ca theo quốc gia",
    labels={"value": "Số ca", "country_region": "Quốc gia", "variable": "Loại"}
)
st.plotly_chart(fig2, use_container_width=True)

# Thông báo kết thúc
st.success("✅ Phân tích hoàn tất! Bạn có thể tiếp tục lọc quốc gia và thời gian để khám phá thêm.")

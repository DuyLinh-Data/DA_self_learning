import streamlit as st
import pandas as pd
import plotly.express as px

# Thiết lập giao diện
st.set_page_config(page_title="Thống kê Covid-19", layout="wide")
st.title("🦠 Phân tích Covid-19 toàn cầu")

# Tải dữ liệu
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/DuyLinh-Data/DA_self_learning/main/Stats_covid19/data/covid_grouped.csv"
    df = pd.read_csv(url)
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# Sidebar lọc dữ liệu
st.sidebar.header("📍 Bộ lọc dữ liệu")
all_countries = df["Country/Region"].unique()
selected_countries = st.sidebar.multiselect("Chọn quốc gia", options=all_countries, default=["Vietnam", "United States", "India"])
metric = st.sidebar.selectbox("Chọn loại thống kê", ["Confirmed", "Recovered", "Deaths"])

filtered_df = df[df["Country/Region"].isin(selected_countries)]

# Biểu đồ theo thời gian
st.subheader(f"📈 {metric} theo thời gian")
fig1 = px.line(
    filtered_df,
    x="Date",
    y=metric,
    color="Country/Region",
    title=f"{metric} theo thời gian",
    markers=True,
)
fig1.update_layout(xaxis_title="Ngày", yaxis_title=metric)
st.plotly_chart(fig1, use_container_width=True)

# Dữ liệu mới nhất
latest_date = df["Date"].max()
latest_df = df[df["Date"] == latest_date]

st.subheader(f"🗺️ {metric} theo bản đồ tại thời điểm {latest_date.date()}")
fig2 = px.scatter_geo(
    latest_df,
    lat="Lat",
    lon="Long",
    color=metric,
    size=metric,
    hover_name="Country/Region",
    projection="natural earth",
    title=f"{metric} trên bản đồ",
)
st.plotly_chart(fig2, use_container_width=True)

# Hiển thị bảng dữ liệu gốc (ẩn mặc định)
with st.expander("📄 Hiển thị dữ liệu gốc"):
    st.dataframe(df)

# Ghi chú
st.markdown("---")
st.markdown("✅ Dữ liệu cập nhật từ GitHub. Bạn có thể chọn quốc gia và loại chỉ số để theo dõi xu hướng Covid-19 toàn cầu.")

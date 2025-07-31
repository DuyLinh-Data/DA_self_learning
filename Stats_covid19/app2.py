import streamlit as st
import pandas as pd
import plotly.express as px

# Cấu hình layout
st.set_page_config(
    page_title="COVID-19 Pandemic Statistics by WHO Region",
    layout="wide"
)

# Tiêu đề
st.title("🌍 COVID-19 WHO Dashboard")
st.markdown("""
Phân tích thống kê **ca nhiễm**, **phục hồi**, **tử vong** theo vùng địa lý WHO từ dữ liệu cập nhật.  
Sử dụng biểu đồ thời gian để theo dõi diễn biến dịch bệnh toàn cầu.
""")

# Load dữ liệu từ GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/DuyLinh-Data/DA_self_learning/main/Stats_covid19/data/covid_grouped.csv"
    df = pd.read_csv(url)
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# Kiểm tra tên cột vùng WHO
who_col = None
for col in df.columns:
    if col.lower() in ["who region", "who_region", "region"]:
        who_col = col
        break

if not who_col:
    st.error("❌ Không tìm thấy cột khu vực WHO trong dữ liệu.")
    st.stop()

# Sidebar lọc dữ liệu
with st.sidebar:
    st.header("⚙️ Bộ lọc")
    regions = sorted(df[who_col].dropna().unique())
    selected_region = st.selectbox("🌐 Chọn vùng WHO", ["Tất cả"] + regions)
    date_range = st.date_input("📅 Khoảng thời gian", 
                               value=[df["Date"].min(), df["Date"].max()],
                               min_value=df["Date"].min(),
                               max_value=df["Date"].max())

# Lọc dữ liệu theo vùng và khoảng thời gian
start_date, end_date = pd.to_datetime(date_range)
df_filtered = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

if selected_region != "Tất cả":
    df_filtered = df_filtered[df_filtered[who_col] == selected_region]

# Tổng hợp theo ngày
df_summary = df_filtered.groupby("Date")[["Confirmed", "Recovered", "Deaths"]].sum().reset_index()

# Hiển thị các chỉ số tổng
latest = df_summary.iloc[-1]
st.subheader(f"📌 Tổng kết đến ngày {latest['Date'].date()}:")
col1, col2, col3 = st.columns(3)
col1.metric("🦠 Tổng ca nhiễm", f"{int(latest['Confirmed']):,}")
col2.metric("💚 Tổng phục hồi", f"{int(latest['Recovered']):,}")
col3.metric("⚰️ Tổng tử vong", f"{int(latest['Deaths']):,}")

# Biểu đồ diễn biến
st.markdown("### 📈 Diễn biến theo thời gian")
fig = px.line(df_summary, x="Date", 
              y=["Confirmed", "Recovered", "Deaths"],
              labels={"value": "Số ca", "Date": "Ngày", "variable": "Loại"},
              title="Thống kê COVID-19 theo thời gian")

st.plotly_chart(fig, use_container_width=True)

# Bảng dữ liệu chi tiết
with st.expander("📄 Xem bảng dữ liệu chi tiết"):
    st.dataframe(df_summary)

st.markdown("---")
st.caption("Nguồn dữ liệu: GitHub - [DuyLinh-Data/DA_self_learning](https://github.com/DuyLinh-Data/DA_self_learning)")

import streamlit as st
import pandas as pd
import plotly.express as px

# Cấu hình layout
st.set_page_config(page_title="COVID-19 Confirmed Cases by WHO Region", layout="wide")
st.title("🦠 Thống kê số ca nhiễm COVID-19 theo khu vực WHO")

# Tải dữ liệu từ raw GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/DuyLinh-Data/DA_self_learning/main/Stats_covid19/data/covid_grouped.csv"
    return pd.read_csv(url)

df = load_data()

# Hiển thị ngày có trong dữ liệu
df["Date"] = pd.to_datetime(df["Date"])
min_date = df["Date"].min()
max_date = df["Date"].max()

# Sidebar chọn ngày
selected_date = st.sidebar.date_input("🗓 Chọn ngày", value=max_date, min_value=min_date, max_value=max_date)
df_filtered = df[df["Date"] == pd.to_datetime(selected_date)]

# Kiểm tra tên cột khu vực WHO
who_col = None
for col in df_filtered.columns:
    if col.lower() in ["who region", "who_region", "region"]:
        who_col = col
        break

if not who_col:
    st.error("❌ Không tìm thấy cột khu vực WHO trong dữ liệu.")
    st.stop()

# Tổng hợp số ca nhiễm theo khu vực WHO
region_data = df_filtered.groupby(who_col)["Confirmed"].sum().reset_index()
region_data = region_data.sort_values("Confirmed", ascending=False)

# Vẽ biểu đồ
fig = px.bar(region_data, 
             x="Confirmed", 
             y=who_col, 
             orientation="h", 
             title=f"Số ca nhiễm theo khu vực WHO - {selected_date}",
             color="Confirmed",
             color_continuous_scale="Reds")

st.plotly_chart(fig, use_container_width=True)

# Hiển thị bảng dữ liệu
with st.expander("📄 Bảng dữ liệu chi tiết"):
    st.dataframe(region_data)

st.markdown("---")
st.caption("Nguồn dữ liệu: GitHub - DA_self_learning")

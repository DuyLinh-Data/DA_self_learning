import streamlit as st
import pandas as pd
import plotly.express as px

# Cấu hình trang
st.set_page_config(page_title="Thống kê COVID-19", layout="wide")
st.title("🦠 Thống kê COVID-19 theo quốc gia")

# Load dữ liệu từ GitHub
@st.cache_data
def load_data():
    url = "https://github.com/DuyLinh-Data/DA_self_learning/blob/main/Stats_covid19/data/covid_grouped.csv"
    return pd.read_csv(url)

df = load_data()

# Tiền xử lý: chọn các cột cần thiết
columns_required = ["Country/Region", "Confirmed", "Recovered", "Deaths", "Date"]
df["Date"] = pd.to_datetime(df["Date"])
df = df[columns_required]

# Sidebar: chọn ngày
min_date = df["Date"].min()
max_date = df["Date"].max()
selected_date = st.sidebar.slider("Chọn ngày", min_value=min_date, max_value=max_date, value=max_date)

# Lọc dữ liệu theo ngày
df_date = df[df["Date"] == selected_date]

# Nhóm theo quốc gia
df_country = df_date.groupby("Country/Region")[["Confirmed", "Recovered", "Deaths"]].sum().reset_index()

# Tabs
tab1, tab2, tab3 = st.tabs(["🟥 Ca nhiễm", "🟩 Phục hồi", "🖤 Tử vong"])

with tab1:
    st.subheader("🟥 Tổng số ca nhiễm theo quốc gia")
    fig = px.choropleth(df_country, locations="Country/Region", locationmode="country names",
                        color="Confirmed", hover_name="Country/Region",
                        color_continuous_scale="Reds", title="Ca nhiễm")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("🟩 Tổng số ca phục hồi theo quốc gia")
    fig = px.choropleth(df_country, locations="Country/Region", locationmode="country names",
                        color="Recovered", hover_name="Country/Region",
                        color_continuous_scale="Greens", title="Phục hồi")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("🖤 Tổng số ca tử vong theo quốc gia")
    fig = px.choropleth(df_country, locations="Country/Region", locationmode="country names",
                        color="Deaths", hover_name="Country/Region",
                        color_continuous_scale="Greys", title="Tử vong")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown(f"📅 Dữ liệu cập nhật đến: **{selected_date.date()}**")

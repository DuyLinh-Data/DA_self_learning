import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Cấu hình giao diện
st.set_page_config(page_title="Product Sales Analysis", layout="wide")

# Tiêu đề ứng dụng
st.title("📊 Product Sales Analysis")

# Đọc dữ liệu từ URL
@st.cache_data
def load_data():
    url = "https://media.geeksforgeeks.org/wp-content/uploads/20240910113410/Order_details-masked.csv"
    return pd.read_csv(url)

df = load_data()

# Hiển thị dữ liệu gốc
with st.expander("📄 Hiển thị dữ liệu gốc"):
    st.dataframe(df)

# Bộ lọc tương tác
st.sidebar.header("🔍 Bộ lọc dữ liệu")
products = st.sidebar.multiselect("Chọn sản phẩm", options=df["Product"].unique(), default=df["Product"].unique())
regions = st.sidebar.multiselect("Chọn khu vực", options=df["Region"].unique(), default=df["Region"].unique())
salespersons = st.sidebar.multiselect("Chọn nhân viên bán hàng", options=df["Salesperson"].unique(), default=df["Salesperson"].unique())

# Lọc dữ liệu theo lựa chọn
filtered_df = df[
    (df["Product"].isin(products)) &
    (df["Region"].isin(regions)) &
    (df["Salesperson"].isin(salespersons))
]

# Tổng quan doanh thu
st.subheader("💰 Tổng quan doanh thu")
col1, col2, col3 = st.columns(3)
col1.metric("Tổng doanh thu", f"${filtered_df['Revenue'].sum():,.2f}")
col2.metric("Tổng số đơn hàng", f"{filtered_df['Order ID'].nunique()}")
col3.metric("Số sản phẩm bán ra", f"{filtered_df['Quantity'].sum()}")

# Doanh thu theo sản phẩm
st.subheader("📦 Doanh thu theo sản phẩm")
revenue_by_product = filtered_df.groupby("Product")["Revenue"].sum().sort_values()
fig1, ax1 = plt.subplots()
sns.barplot(x=revenue_by_product.values, y=revenue_by_product.index, ax=ax1)
ax1.set_xlabel("Doanh thu")
ax1.set_ylabel("Sản phẩm")
st.pyplot(fig1)

# Doanh thu theo khu vực
st.subheader("🌍 Doanh thu theo khu vực")
revenue_by_region = filtered_df.groupby("Region")["Revenue"].sum().reset_index()
fig2 = px.pie(revenue_by_region, names="Region", values="Revenue", title="Tỷ lệ doanh thu theo khu vực")
st.plotly_chart(fig2)

# Doanh thu theo nhân viên
st.subheader("🧑‍💼 Doanh thu theo nhân viên bán hàng")
revenue_by_salesperson = filtered_df.groupby("Salesperson")["Revenue"].sum().sort_values()
fig3, ax3 = plt.subplots()
sns.barplot(x=revenue_by_salesperson.values, y=revenue_by_salesperson.index, ax=ax3)
ax3.set_xlabel("Doanh thu")
ax3.set_ylabel("Nhân viên")
st.pyplot(fig3)

# Phân tích theo thời gian
st.subheader("📅 Doanh thu theo thời gian")
filtered_df["Order Date"] = pd.to_datetime(filtered_df["Order Date"])
revenue_by_month = filtered_df.groupby(filtered_df["Order Date"].dt.to_period("M"))["Revenue"].sum().reset_index()
revenue_by_month["Order Date"] = revenue_by_month["Order Date"].dt.to_timestamp()
fig4 = px.line(revenue_by_month, x="Order Date", y="Revenue", markers=True, title="Doanh thu theo tháng")
st.plotly_chart(fig4)

# Kết luận
st.markdown("---")
st.markdown("✅ **Ứng dụng phân tích doanh số sản phẩm hoàn tất. Bạn có thể điều chỉnh bộ lọc để khám phá thêm thông tin chi tiết.**")

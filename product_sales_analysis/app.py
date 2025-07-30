import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cấu hình giao diện rộng
st.set_page_config(page_title="Phân Tích Doanh Số Sản Phẩm", layout="wide")

# Tiêu đề chính
st.title("📊 Phân tích doanh số bán hàng theo sản phẩm")

# Tải dữ liệu
@st.cache_data
def load_data():
    url = "https://media.geeksforgeeks.org/wp-content/uploads/20240910113410/Order_details-masked.csv"
    return pd.read_csv(url)

df = load_data()

# Hiển thị dữ liệu gốc
with st.expander("📄 Xem dữ liệu gốc"):
    st.dataframe(df)

# Kiểm tra cột hiện có
columns = df.columns.tolist()
st.sidebar.write("🧾 Các cột hiện có:", columns)

# Kiểm tra xem các cột có tồn tại không
required_cols = ['Product', 'Revenue', 'Quantity', 'Order Date']
if not all(col in df.columns for col in required_cols):
    st.error("❌ Dữ liệu không đủ cột để phân tích. Vui lòng kiểm tra file CSV.")
    st.stop()

# Bộ lọc sản phẩm
products = st.sidebar.multiselect(
    "🛍 Chọn sản phẩm",
    options=df["Product"].unique(),
    default=df["Product"].unique()
)

# Lọc dữ liệu
df_filtered = df[df["Product"].isin(products)]

# Tổng quan
st.subheader("📈 Tổng quan doanh thu và số lượng")
col1, col2 = st.columns(2)
col1.metric("💰 Tổng doanh thu", f"${df_filtered['Revenue'].sum():,.2f}")
col2.metric("📦 Sản phẩm bán ra", int(df_filtered["Quantity"].sum()))

# Doanh thu theo sản phẩm
st.subheader("🧾 Doanh thu theo từng sản phẩm")
revenue_by_product = df_filtered.groupby("Product")["Revenue"].sum().sort_values()
fig1, ax1 = plt.subplots()
sns.barplot(x=revenue_by_product.values, y=revenue_by_product.index, ax=ax1)
ax1.set_xlabel("Doanh thu ($)")
ax1.set_ylabel("Sản phẩm")
st.pyplot(fig1)

# Số lượng bán theo sản phẩm
st.subheader("📊 Số lượng sản phẩm bán ra")
quantity_by_product = df_filtered.groupby("Product")["Quantity"].sum().sort_values()
fig2, ax2 = plt.subplots()
sns.barplot(x=quantity_by_product.values, y=quantity_by_product.index, ax=ax2)
ax2.set_xlabel("Số lượng")
ax2.set_ylabel("Sản phẩm")
st.pyplot(fig2)

# Phân tích theo thời gian
st.subheader("🕒 Doanh thu theo thời gian")
df_filtered["Order Date"] = pd.to_datetime(df_filtered["Order Date"])
monthly_revenue = df_filtered.groupby(df_filtered["Order Date"].dt.to_period("M"))["Revenue"].sum()
monthly_revenue.index = monthly_revenue.index.to_timestamp()
fig3, ax3 = plt.subplots()
monthly_revenue.plot(kind='line', marker='o', ax=ax3)
ax3.set_title("Doanh thu theo tháng")
ax3.set_xlabel("Thời gian")
ax3.set_ylabel("Doanh thu ($)")
st.pyplot(fig3)

# Kết thúc
st.success("✅ Phân tích hoàn tất! Bạn có thể lọc để xem chi tiết.")


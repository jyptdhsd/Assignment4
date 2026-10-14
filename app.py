import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Zhou Yunyi", layout="wide")
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

@st.cache_data
def load_data():
    df = pd.read_csv("KFC_Past_Sales_Dataset.csv")
    df["Month_Number"] = pd.Categorical(df["Month"], categories=MONTHS, ordered=True).codes + 1
    df["Date"] = pd.to_datetime(dict(year=df["Year"], month=df["Month_Number"], day=1))
    return df

df = load_data()
st.title("Zhou Yunyi")
st.write("For a KFC regional operations manager: identify weaker-performing branches and prioritize operational reviews.")
st.caption("Source: Kaggle KFC Global Sales Dataset (2018–2024) | Historical snapshot: 2018–2024 | Proposed production refresh: nightly; manager review: weekly. Currency is unspecified; monetary values shown in dataset units.")

countries = sorted(df["Country"].unique())
country = st.selectbox("Country", countries)
subset = df[df["Country"] == country].copy()
branch = st.selectbox("Branch", ["All branches"] + sorted(subset["Branch_ID"].unique().tolist()))
if branch != "All branches":
    subset = subset[subset["Branch_ID"] == branch]

sales = subset["Sales"].sum()
customers = subset["Customers"].sum()
per_customer = sales / customers if customers else 0
c1, c2, c3 = st.columns(3)
c1.metric("Total sales (dataset units)", f"{sales:,.0f}")
c2.metric("Total customers (reported)", f"{customers:,.0f}")
c3.metric("Sales per customer", f"{per_customer:,.2f}")

monthly = subset.groupby("Date", as_index=False)["Sales"].sum().sort_values("Date")
fig, ax = plt.subplots(figsize=(10, 3.3))
ax.plot(monthly["Date"], monthly["Sales"], linewidth=2)
ax.set_title("Monthly sales trend")
ax.set_ylabel("Sales (dataset units)")
ax.set_xlabel("Month")
ax.grid(alpha=0.2)
fig.autofmt_xdate()
st.pyplot(fig)
plt.close(fig)

st.subheader("Branch comparison")
branch_summary = subset.groupby("Branch_ID", as_index=False).agg(Sales=("Sales", "sum"), Customers=("Customers", "sum"), Records=("Sales", "size"))
branch_summary["Sales_per_record"] = branch_summary["Sales"] / branch_summary["Records"]
branch_summary = branch_summary.sort_values("Sales_per_record", ascending=True)
fig2, ax2 = plt.subplots(figsize=(10, max(2.5, len(branch_summary) * 0.48)))
ax2.barh(branch_summary["Branch_ID"], branch_summary["Sales_per_record"])
ax2.set_xlabel("Average sales per record (dataset units)")
ax2.set_title("Branch performance normalized by record count")
st.pyplot(fig2)
plt.close(fig2)

with st.expander("Data notes and detailed branch figures"):
    st.write("Multiple records share the same year, month, and branch. Their underlying grain is not documented, so records are retained and summed rather than deduplicated. Customer counts may not represent unique people. Marketing spending is not evidence of causal impact. This is a static historical sample, not live KFC data.")
    st.dataframe(branch_summary.sort_values("Sales_per_record"), use_container_width=True, hide_index=True)

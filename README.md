# Assignment4
# KFC Global Sales Performance Dashboard

**Team:** [Add team name and at least four members]  
**App:** [Add public Streamlit URL after deployment]  
**Dataset:** [KFC Global Sales Dataset (2018–2024)](https://www.kaggle.com/datasets/usman44m/kfc-global-sales-dataset-20182024)

## Step 1 — Dataset and decision maker

We chose a compact, tabular historical sales dataset to study recurring restaurant operations decisions. The supplied CSV has 8,000 rows, seven columns, no missing values, and observations labeled 2018–2024 across five countries and 13 branch identifiers. Fields are Year, Month, Country, Branch_ID, Sales, Customers, and Marketing_Spend. The supplied CSV is approximately 349 KB, well below 25 MB. The Kaggle dataset is not verified as official KFC transaction data; whether it is synthetic and its precise record grain must be confirmed from the publisher's documentation. We therefore treat it as a classroom case study, not as an audited corporate report.

**Specific audience:** a KFC regional operations manager overseeing branches within one country. This person can compare branch performance and decide where to investigate staffing, local demand, or operating practices.

## Step 2 — Why a dashboard?

**Who and how often?** The regional operations manager reviews it every Monday before the weekly branch performance meeting, and may revisit it when a branch requires investigation.

**Actionable decision:** If the manager sees a branch consistently producing less sales per recorded observation than its peers, they will investigate that branch's demand, staffing, and operational constraints before deciding on a corrective action. The metric is a screening signal, not proof of poor management.

**Without it:** The manager must export files, filter countries and branches, manually calculate totals, and compare time periods in a spreadsheet. This introduces repetitive work and risks inconsistent comparisons. We cannot credibly quantify money or time saved from this dataset alone.

**Why not a weekly email?** A static email cannot quickly switch between a country-wide view and a specific branch, nor allow a manager to explore which months explain an unexpected pattern. The dashboard supports repeated interactive comparisons. A weekly alert can complement it but does not replace the exploratory view.

## Step 3 — What matters and what is excluded?

**EDA performed:** `eda.ipynb` checks shape, types, missing values, distributions, repeated branch-month keys, outliers, and relationships between sales, customers, and marketing spending.

**Top of page: three KPIs.** Total Sales indicates sales scale, Total Customers indicates recorded traffic, and Sales per Customer indicates average sales intensity. They appear first so the manager can quickly understand the selected scope. Because no currency is specified, sales use dataset units, not USD.

**Middle: two explanatory charts.** A monthly sales trend shows when sales change; a branch comparison shows average sales per record to reduce distortion from unequal record counts. This normalization is imperfect because the dataset does not document the underlying record grain. For a single selected branch, the second chart provides a single-branch reference rather than a peer comparison.

**Useful filters:** Country is primary because the manager works in one market. Branch allows focused follow-up. We deliberately omit excessive sliders and demographic controls.

**Two excluded items:** (1) A marketing ROI KPI: the dataset has spending and sales but no campaign attribution or incremental sales estimates, so calling the ratio ROI would be misleading. (2) A country leaderboard: our target user manages one country, and cross-country monetary units may not be comparable.

**Limitations and mitigations:** The data contain multiple rows for the same Year–Month–Branch combination; these are not deleted because they may represent distinct underlying records. We aggregate sales and reported customers for KPI totals and monthly trends and normalize branch comparisons by record count. We do not claim the customer counts are unique individuals. The CSV has no currency, unit conversion, sales targets, or live timestamps. A high sales–marketing association would not establish causality. The interface labels monetary values as dataset units and discloses the historical snapshot.

**Top-to-bottom order:** KPI row → monthly trend → branch comparison → expandable detail and limitations. This places rapid assessment before explanation and keeps deeper context below the fold.

## Step 4 — Refresh and action thresholds

**Production data refresh:** Nightly, after point-of-sale data are consolidated and validated. A real deployment would require consistent country currencies, branch identifiers, and record-level timestamps. Live minute-by-minute refresh would add cost without changing the weekly management decision.

**Review frequency:** Every Monday, separately from nightly data updates. A data refresh is not the same as a managerial review.

**Tracked metric:** Weekly branch sales per recorded observation, compared with the branch's trailing four comparable weeks (after reliable record grain and dates are available). **Proposed action rule:** If the metric falls more than 15% below that baseline for two consecutive completed weeks, the manager requests a branch review. This is a proposed operational threshold, not one validated by the historical data; it is not implemented as a live alert in this static demo.

**Cost of stale data:** One stale day is usually tolerable for a Monday review; a week of stale data could hide a sustained sales decline and delay corrective action. The current Kaggle file is a frozen historical snapshot and does not simulate fresh updates.

## Step 5 — Build and deploy

Project files: `app.py`, `requirements.txt`, `KFC_Past_Sales_Dataset.csv`, and this README.

1. Create a public GitHub repository and upload these files.
2. In Streamlit Community Cloud, create a new app from the repository, with `app.py` as the entry point.
3. In advanced settings, select Python **3.14** as instructed by the course, then deploy. Check dependency compatibility if installation fails.
4. Test both filters and verify KPI totals against the notebook; paste the deployed URL and team members above.

Local run: `pip install -r requirements.txt` then `streamlit run app.py`.

**Note:** A live GitHub repository and public Streamlit URL require deployment from a team member's account; neither is created by the supplied files.


# 🧠 data-science-snippets

A modular collection of Python snippets for faster, cleaner, and more effective data science workflows — organized by task: EDA, cleaning, preprocessing, loading, and more.

---

## 📁 Folder Structure
<pre> 
data-science-snippets/
├── eda/
│   ├── main.py 
├── data_cleaning/
│   ├── missing_data_summary.py
│   └── outlier_detection.py
├── preprocessing/
│   ├── minmax_scaling.py
│   └── encoding.py
├── loading/
│   ├── load_csv_with_info.py
│   └── safe_parquet_loader.py
├── visualization/
│   ├── missing_data_heatmap.py
│   └── distribution_plot.py
└── README.md
</pre>

----

## 🔹 `eda/` – Exploratory Data Analysis

- `main.py`: Shows the most common (modal) value in each column, frequency, and % of non-null values, basic stats and quick structure overview (dtypes, cardinality, etc.).
 
## 🔹 `data_cleaning/`

- `missing_data_summary.py`: Shows total/percentage of missing values per column + data types.
- `outlier_detection.py`: IQR or z-score based detection functions.

## 🔹 `preprocessing/`

- `minmax_scaling.py`: Scale numeric columns between 0 and 1.
- `encoding.py`: Label or one-hot encoding helpers for categorical columns.

## 🔹 `loading/`

- `load_csv_with_info.py`: Load CSVs with column summaries printed instantly.
- `safe_parquet_loader.py`: Robust loading for large parquet datasets.

## 🔹 `visualization/`

- `missing_data_heatmap.py`: Visual heatmap of missing values using Seaborn.
- `distribution_plot.py`: Compare distributions before/after scaling.

---

## 🛠️ Usage

You can import any snippet directly or convert them to utility classes/functions.

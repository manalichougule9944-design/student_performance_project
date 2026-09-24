import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# ==========================================
# 1. LOAD DATA
# ==========================================
df = pd.read_csv("data/student_performance_100.csv")
print("DATA LOADED SUCCESSFULLY")
print("=" * 50)
# ==========================================
# 2. UNDERSTAND THE DATA
# ==========================================
print("\nFirst 5 rows:")
print(df.head())
print("\nDataset Shape:")
print(df.shape)
print("\nColumn Information:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())
# ==========================================
# 3. DATA CLEANING
# ==========================================
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Rows:")
print(df.duplicated().sum())
# Remove duplicates
df = df.drop_duplicates()
# ==========================================
# 4. EDA
# ==========================================
print("\nAverage Final Marks:")
print(df["Final_Marks"].mean())
print("\nAverage Attendance:")
print(df["Attendance_Pct"].mean())
print("\nAverage Study Hours:")
print(df["Study_Hours_Per_Day"].mean())
print("\nResult Distribution:")
print(df["Result"].value_counts())
print("\nDepartment Performance:")
department_summary = df.groupby("Department")["Final_Marks"].agg(
    ["count", "mean", "min", "max"]
)
print(department_summary.round(2))
# ==========================================
# 5. TOP STUDENTS
# ==========================================
print("\nTop 10 Students:")
top_students = df.sort_values(
    "Final_Marks",
    ascending=False
).head(10)
print(
    top_students[
        [
            "Student_ID",
            "Department",
            "Attendance_Pct",
            "Study_Hours_Per_Day",
            "Final_Marks"
        ]
    ]
)
# ==========================================
# 6. CORRELATION
# ==========================================
study_correlation = df[
    "Study_Hours_Per_Day"
].corr(
    df["Final_Marks"]
)
attendance_correlation = df[
    "Attendance_Pct"
].corr(
    df["Final_Marks"]
)
print("\nStudy Hours vs Final Marks Correlation:")
print(round(study_correlation, 2))
print("\nAttendance vs Final Marks Correlation:")
print(round(attendance_correlation, 2))
# ==========================================
# 7. VISUALIZATION 1
# ==========================================
plt.figure(figsize=(8, 5))
sns.histplot(
    df["Final_Marks"],
    bins=10,
    kde=True
)
plt.title("Distribution of Final Marks")
plt.xlabel("Final Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()
# ==========================================
# 8. VISUALIZATION 2
# ==========================================
plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="Department",
    y="Final_Marks"
)
plt.title("Final Marks by Department")
plt.xlabel("Department")
plt.ylabel("Final Marks")
plt.tight_layout()
plt.show()
# ==========================================
# 9. VISUALIZATION 3
# ==========================================
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Study_Hours_Per_Day",
    y="Final_Marks",
    hue="Result"
)
plt.title("Study Hours vs Final Marks")
plt.xlabel("Study Hours per Day")
plt.ylabel("Final Marks")
plt.tight_layout()
plt.show()
# ==========================================
# 10. VISUALIZATION 4
# ==========================================
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Attendance_Pct",
    y="Final_Marks",
    hue="Result"
)
plt.title("Attendance vs Final Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Final Marks")
plt.tight_layout()
plt.show()
# ==========================================
# 11. CORRELATION HEATMAP
# ==========================================
numeric_columns = df.select_dtypes(
    include=np.number
)
correlation_matrix = numeric_columns.corr()
plt.figure(figsize=(10, 7))
sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
print("\nAnalysis completed successfully!")
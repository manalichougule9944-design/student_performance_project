import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path


# ==========================================
# FILE PATHS
# ==========================================

DATA_PATH = Path("data/student_performance_100.csv")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_PATH = OUTPUT_DIR / "dashboard.html"


# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv(DATA_PATH)


# ==========================================
# KPI CALCULATIONS
# ==========================================

total_students = len(df)

average_marks = df["Final_Marks"].mean()

pass_rate = (
    df["Result"].eq("Pass").mean()
) * 100

average_attendance = (
    df["Attendance_Pct"].mean()
)

average_study_hours = (
    df["Study_Hours_Per_Day"].mean()
)


# ==========================================
# DEPARTMENT SUMMARY
# ==========================================

department_summary = (
    df.groupby("Department")
    .agg(
        Students=("Student_ID", "count"),
        Average_Marks=("Final_Marks", "mean"),
        Average_Attendance=("Attendance_Pct", "mean")
    )
    .reset_index()
)


# ==========================================
# CHART 1
# DEPARTMENT PERFORMANCE
# ==========================================

fig_department = px.bar(
    department_summary,
    x="Department",
    y="Average_Marks",
    text="Average_Marks",
    title="Average Final Marks by Department"
)

fig_department.update_traces(
    texttemplate="%{text:.1f}",
    textposition="outside"
)

fig_department.update_layout(
    template="plotly_white",
    height=400
)


# ==========================================
# CHART 2
# RESULT DISTRIBUTION
# ==========================================

result_counts = (
    df["Result"]
    .value_counts()
    .reset_index()
)

result_counts.columns = [
    "Result",
    "Students"
]

fig_result = px.pie(
    result_counts,
    names="Result",
    values="Students",
    hole=0.45,
    title="Student Result Distribution"
)

fig_result.update_layout(
    template="plotly_white",
    height=400
)


# ==========================================
# CHART 3
# STUDY HOURS VS MARKS
# ==========================================

fig_study = px.scatter(
    df,
    x="Study_Hours_Per_Day",
    y="Final_Marks",
    color="Department",
    hover_data=[
        "Student_ID",
        "Attendance_Pct",
        "Backlogs",
        "Result"
    ],
    title="Study Hours vs Final Marks"
)

fig_study.update_layout(
    template="plotly_white",
    height=450
)


# ==========================================
# CHART 4
# ATTENDANCE VS MARKS
# ==========================================

fig_attendance = px.scatter(
    df,
    x="Attendance_Pct",
    y="Final_Marks",
    color="Result",
    hover_data=[
        "Student_ID",
        "Department",
        "Study_Hours_Per_Day"
    ],
    title="Attendance vs Final Marks"
)

fig_attendance.update_layout(
    template="plotly_white",
    height=450
)


# ==========================================
# CHART 5
# MARK DISTRIBUTION
# ==========================================

fig_distribution = px.histogram(
    df,
    x="Final_Marks",
    nbins=12,
    color="Result",
    title="Distribution of Final Marks"
)

fig_distribution.update_layout(
    template="plotly_white",
    height=450
)


# ==========================================
# CHART 6
# CORRELATION HEATMAP
# ==========================================

numeric_data = df.select_dtypes(
    include=np.number
)

correlation = numeric_data.corr()

fig_correlation = px.imshow(
    correlation,
    text_auto=".2f",
    aspect="auto",
    title="Correlation Heatmap"
)

fig_correlation.update_layout(
    template="plotly_white",
    height=550
)


# ==========================================
# TOP 10 STUDENTS
# ==========================================

top_students = (
    df.sort_values(
        "Final_Marks",
        ascending=False
    )
    .head(10)
)

top_students = top_students[
    [
        "Student_ID",
        "Department",
        "Attendance_Pct",
        "Study_Hours_Per_Day",
        "Final_Marks",
        "Result"
    ]
]


# Convert table to HTML
table_html = top_students.to_html(
    index=False,
    classes="student-table",
    border=0
)


# ==========================================
# INSIGHTS
# ==========================================

best_department = department_summary.loc[
    department_summary["Average_Marks"].idxmax(),
    "Department"
]

lowest_department = department_summary.loc[
    department_summary["Average_Marks"].idxmin(),
    "Department"
]

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


insights_html = f"""
<ul>
    <li>
        <b>{best_department}</b> has the highest
        average final marks.
    </li>

    <li>
        <b>{lowest_department}</b> has the lowest
        average final marks.
    </li>

    <li>
        Study hours and final marks have a
        correlation of <b>{study_correlation:.2f}</b>.
    </li>

    <li>
        Attendance and final marks have a
        correlation of <b>{attendance_correlation:.2f}</b>.
    </li>

    <li>
        Overall student pass rate is
        <b>{pass_rate:.1f}%</b>.
    </li>
</ul>
"""


# ==========================================
# CONVERT CHART TO HTML
# ==========================================

def chart_html(fig):

    return fig.to_html(
        full_html=False,
        include_plotlyjs=False
    )


# ==========================================
# COMPLETE HTML DASHBOARD
# ==========================================

html = f"""

<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>
Student Performance Analytics Dashboard
</title>

<script src=
"https://cdn.plot.ly/plotly-2.35.2.min.js">
</script>


<style>

body {{

    margin: 0;

    font-family:
    Arial, sans-serif;

    background: #f4f6f8;

    color: #222;
}}


.header {{

    background: #1f2937;

    color: white;

    padding: 25px 40px;
}}


.header h1 {{

    margin: 0;

    font-size: 30px;
}}


.header p {{

    margin-top: 8px;

    opacity: 0.8;
}}


.container {{

    max-width: 1400px;

    margin: auto;

    padding: 25px;
}}


.kpis {{

    display: grid;

    grid-template-columns:
    repeat(4, 1fr);

    gap: 20px;

    margin-bottom: 25px;
}}


.card {{

    background: white;

    padding: 20px;

    border-radius: 12px;

    box-shadow:
    0 2px 8px rgba(0,0,0,0.08);
}}


.card .label {{

    color: #6b7280;

    font-size: 14px;
}}


.card .value {{

    font-size: 30px;

    font-weight: bold;

    margin-top: 8px;
}}


.grid {{

    display: grid;

    grid-template-columns:
    1fr 1fr;

    gap: 20px;
}}


.chart {{

    background: white;

    border-radius: 12px;

    padding: 10px;

    box-shadow:
    0 2px 8px rgba(0,0,0,0.08);
}}


.full {{

    grid-column:
    1 / -1;
}}


.insights {{

    margin-top: 25px;

    background: white;

    padding: 25px;

    border-radius: 12px;

    box-shadow:
    0 2px 8px rgba(0,0,0,0.08);
}}


.student-table {{

    width: 100%;

    border-collapse:
    collapse;
}}


.student-table th,
.student-table td {{

    padding: 10px;

    border-bottom:
    1px solid #ddd;

    text-align: left;
}}


.student-table th {{

    background: #f3f4f6;
}}


@media(max-width: 900px) {{

    .kpis,
    .grid {{

        grid-template-columns:
        1fr;
    }}

    .full {{

        grid-column: auto;
    }}
}}

</style>

</head>


<body>


<div class="header">

<h1>
Student Performance Analytics Dashboard
</h1>

<p>
Python • Pandas • Plotly • 100 Students
</p>

</div>


<div class="container">


<!-- KPI SECTION -->

<div class="kpis">


<div class="card">

<div class="label">
Total Students
</div>

<div class="value">
{total_students}
</div>

</div>


<div class="card">

<div class="label">
Average Final Marks
</div>

<div class="value">
{average_marks:.1f}
</div>

</div>


<div class="card">

<div class="label">
Pass Rate
</div>

<div class="value">
{pass_rate:.1f}%
</div>

</div>


<div class="card">

<div class="label">
Average Attendance
</div>

<div class="value">
{average_attendance:.1f}%
</div>

</div>


</div>


<!-- CHARTS -->

<div class="grid">


<div class="chart">

{chart_html(fig_department)}

</div>


<div class="chart">

{chart_html(fig_result)}

</div>


<div class="chart">

{chart_html(fig_study)}

</div>


<div class="chart">

{chart_html(fig_attendance)}

</div>


<div class="chart">

{chart_html(fig_distribution)}

</div>


<div class="chart">

{chart_html(fig_correlation)}

</div>


<!-- TOP STUDENTS -->

<div class="chart full">

<h2>
Top 10 Students
</h2>

{table_html}

</div>


</div>


<!-- INSIGHTS -->

<div class="insights">

<h2>
Key Insights
</h2>

{insights_html}

</div>


</div>


</body>

</html>

"""


# ==========================================
# SAVE DASHBOARD
# ==========================================

OUTPUT_PATH.write_text(
    html,
    encoding="utf-8"
)


print()
print("=" * 50)
print("DASHBOARD CREATED SUCCESSFULLY")
print("=" * 50)

print(
    f"Open this file in your browser:"
)

print(
    OUTPUT_PATH
)
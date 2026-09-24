# Student Performance & Engagement Analytics Dashboard

## 📌 Project Overview

This mini-project is designed for **3rd-semester students** to learn the complete data analysis workflow using Python and AI-assisted analysis.

Students will work with a dataset containing information about student attendance, study hours, assignment scores, internal marks, lab scores, backlogs, screen time, placement interest, and final marks.

The project covers:

**CSV Data → Data Cleaning → Exploratory Data Analysis → Visualization → AI-Assisted Insights → Interactive HTML Dashboard**

> **Note:** This project does not use Streamlit. The dashboard is created using **Plotly** and saved as an interactive HTML file.

---

## 🎯 Project Objectives

By completing this project, students will learn how to:

* Load CSV data using Pandas
* Understand the structure of a dataset
* Identify missing values and duplicate records
* Perform basic data cleaning
* Calculate descriptive statistics
* Group and analyze data using Pandas
* Find relationships between variables
* Create charts using Seaborn and Plotly
* Use AI tools to assist with data analysis
* Build an interactive HTML dashboard
* Present data-driven insights

---

## 🛠️ Technologies Used

| Technology   | Purpose                                    |
| ------------ | ------------------------------------------ |
| Python       | Programming language                       |
| Pandas       | Data manipulation and analysis             |
| NumPy        | Numerical operations                       |
| Matplotlib   | Data visualization                         |
| Seaborn      | Statistical visualization                  |
| Plotly       | Interactive charts and dashboard           |
| VS Code      | Development environment                    |
| AI Assistant | Analysis assistance and insight generation |

---

## 📂 Project Structure

```text
student_performance_project/
│
├── data/
│   └── student_performance_100.csv
│
├── output/
│   └── dashboard.html
│
├── src/
│   ├── analysis.py
│   └── dashboard.py
│
├── requirements.txt
└── README.md
```

### Folder Description

### `data/`

Contains the input dataset:

```text
student_performance_100.csv
```

The dataset contains 100 student records.

### `src/`

Contains the Python programs.

**`analysis.py`**

Used for:

* Loading the dataset
* Exploring the data
* Checking missing values
* Checking duplicates
* Calculating statistics
* Performing groupby analysis
* Finding correlations
* Creating basic visualizations

**`dashboard.py`**

Used to:

* Calculate dashboard KPIs
* Create interactive Plotly charts
* Generate key insights
* Create the final HTML dashboard

### `output/`

Contains the generated dashboard:

```text
dashboard.html
```

---

# 📊 Dataset

The dataset contains the following columns:

| Column              | Description                                 |
| ------------------- | ------------------------------------------- |
| Student_ID          | Unique student identifier                   |
| Gender              | Student gender                              |
| Age                 | Student age                                 |
| Department          | Student department                          |
| Attendance_Pct      | Attendance percentage                       |
| Study_Hours_Per_Day | Average study hours per day                 |
| Assignment_Score    | Assignment score                            |
| Internal_Marks      | Internal assessment marks                   |
| Lab_Score           | Laboratory score                            |
| Backlogs            | Number of backlogs                          |
| Screen_Time_Hours   | Average daily screen time                   |
| Placement_Interest  | Whether student is interested in placements |
| Final_Marks         | Final examination marks                     |
| Result              | Student result category                     |

---

# ⚙️ Installation

## Step 1: Install Python

Make sure Python is installed.

Check Python version:

```bash
python --version
```

If that does not work on Windows, try:

```bash
py --version
```

---

## Step 2: Open the Project in VS Code

Open the project folder:

```text
student_performance_project
```

in Visual Studio Code.

---

## Step 3: Open the Terminal

In VS Code:

**Terminal → New Terminal**

---

## Step 4: Create a Virtual Environment

Run:

```bash
python -m venv venv
```

---

## Step 5: Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

After activation, you should see something similar to:

```text
(venv)
```

in the terminal.

---

## Step 6: Install Required Libraries

Run:

```bash
pip install -r requirements.txt
```

The required libraries are:

```text
pandas
numpy
matplotlib
seaborn
plotly
statsmodels
```

---

# 🔍 Running the Data Analysis

From the project root folder, run:

```bash
python src/analysis.py
```

The program will:

1. Load the CSV file
2. Display the first few records
3. Display dataset dimensions
4. Check column information
5. Display statistical summary
6. Check missing values
7. Check duplicate records
8. Calculate average marks
9. Calculate average attendance
10. Calculate average study hours
11. Analyze results
12. Analyze department performance
13. Display top-performing students
14. Calculate correlations
15. Generate visualizations

---

# 📈 Running the Dashboard

After completing the analysis, run:

```bash
python src/dashboard.py
```

If successful, you should see a message similar to:

```text
Dashboard created successfully!
```

The following file will be generated:

```text
output/dashboard.html
```

---

# 🌐 Opening the Dashboard

## Option 1: Using VS Code Live Server

Recommended method.

### Step 1

Install the **Live Server** extension in VS Code.

### Step 2

Open:

```text
output/dashboard.html
```

### Step 3

Right-click inside the HTML file.

Select:

```text
Open with Live Server
```

The dashboard will open in your browser.

---

## Option 2: Open Directly

You can also open:

```text
output/dashboard.html
```

directly in a web browser.

However, **Live Server is recommended** for the workshop.

---

# 📊 Dashboard Features

The dashboard contains:

### KPI Cards

* Total Students
* Average Final Marks
* Pass Rate
* Average Attendance
* Average Study Hours

### Visualizations

#### 1. Average Final Marks by Department

Shows how average performance differs between departments.

#### 2. Result Distribution

Shows the proportion of students in each result category.

#### 3. Study Hours vs Final Marks

Helps explore the relationship between study time and final marks.

#### 4. Attendance vs Final Marks

Helps explore the relationship between attendance and academic performance.

#### 5. Final Marks Distribution

Shows how final marks are distributed across students.

#### 6. Correlation Heatmap

Shows relationships between numerical variables.

#### 7. Top 10 Students

Displays students with the highest final marks.

#### 8. Key Insights

Displays automatically generated observations based on the dataset.

---

# 🤖 AI-Assisted Analysis

AI can be used as an **assistant**, not as a replacement for analysis.

Students can use ChatGPT or another AI assistant to understand the dataset and generate ideas.

### Example Prompt 1

```text
I have a student performance dataset with columns such as
attendance, study hours, assignment score, internal marks,
backlogs and final marks.

Suggest 5 useful questions that I can answer using exploratory
data analysis.
```

### Example Prompt 2

```text
Suggest suitable charts for analyzing the relationship between
attendance, study hours, backlogs and final marks.

Explain why each chart would be useful.
```

### Example Prompt 3

```text
The correlation between study hours and final marks is 0.65.

Explain what this correlation means in simple terms.
Also explain why correlation does not prove causation.
```

### Example Prompt 4

```text
Here are my calculated results:

Average attendance: 78%
Average study hours: 4.2 hours
Average final marks: 69
Pass rate: 82%

Generate 3 short data-driven observations.
Do not invent any information that is not provided.
```

---

# 🧹 Data Cleaning Tasks

Students should check:

* Missing values
* Duplicate records
* Incorrect data types
* Unusual values
* Invalid ranges
* Outliers

For example:

```python
df.isnull().sum()
```

To check duplicates:

```python
df.duplicated().sum()
```

To remove duplicate records:

```python
df = df.drop_duplicates()
```

---

# 🔎 Exploratory Data Analysis

Students should answer questions such as:

### Question 1

Which department has the highest average final marks?
gskj;lgsjkkjlf;,fcw
### Question 2

Does higher attendance appear to be associated with higher final marks?

### Question 3

Does study time appear to be related to final marks?

### Question 4

How many students have backlogs?

### Question 5

What percentage of students passed?

### Question 6

Which students have the highest final marks?

---

# 🎨 Mini Dashboard Customization

Students should modify at least **3 things** in the dashboard.

For example:

### Task 1

Change the dashboard titvzmklvjdvmkle.

### Task 2

Add a new KPI:

```text
Average Assignment Score
```

### Task 3

Add a new chart:

```textvdksalmvlkdsa;
Average Study Hours by Department
```

### Optional Tasks

Students can also add:

* Pass rate by department
* Average attendance by department
* Backlogs by department
* Top 5 students
* Students with attendance below 70%
* Students with two or more backlogs
vmkfdl;svmj
---

# 🧠 Important Data Analysis Concepts

Students should understand the difference between:

### Mean

Average value of a variable.

### Median

Middle value when data is arranged in order.

### Correlation

Measures the strength and direction of a relationship between two numerical variables.

### Important

**Correlation does not mean causation.**

For example, if study hovmkfld;sgvjoierwurs and final marks have a positive correlation, it does not automatically prove that studying more caused higher marks.

---

# 📝 Final Project Presentation
vfkds;lmv
Each group/student should present the following:

## 1. Problem Statement

What problem are we trying to understand?

## 2. Dataset

What data was used?

## 3. Data Cleaning

What cleaning steps were performed?

## 4. EDA

What patterns were discovered?
vkfml;wgv
## 5. Visualizations

Which charts were created and why?

## 6. Dashboard

Demonstrate the interactive dashboard.

## 7. Key Insights

Present at least **3 important observations**.

## 8. Limitations
mvkcds;
Explain limitations of the analysis.

Example:

* Dataset contains only 100 students.
* Data is simulated for educational purposes.
* Correlation does not prove causation.
* More semesters could provide better insights.
mkl;vfj
---

# ⏱️ Suggested 3–3.5 Hour Mini-Project Plan

| Time   | Activity                  |
| ------ | ------------------------- |
| 15 min | Understand the problem    |
| 20 min | Load and explore dataset  |
| 25 min | Data cleaning             |
| 35 min | Exploratory dmkl;akfierata analysis |
| 25 min | Create visualizations     |
| 40 min | Build/customize dashboard |
| 20 min | AI-assisted insights      |
| 15 min | Final presentation        |

---

# 🎓 Learning Outcome

After completing this project, students should be able to explain and demonstrate the basic data analysis workflow:

```text
Collect
   ↓ik,mv;lkdc'kvz 
Understand
   ↓
Clean
   ↓
Analyze
   ↓
Visualize
   ↓
Interpret
   ↓
Communicate
```

They will also understanf9oiv kmvc/mx;'dfkopergd how AI tools can assist with:

* Generating analysis questions
* Explaining statistical concepts
* Suggesting visualizations
* Writing or improving Python code
* Summarizing findings

---

# ⚠️ Important Notes

* The dataset is intended for **educational purposes**.
* Students should verifykop AI-generated code and insights.
* Do not blindly copy AI-generated conclusions.
* Always check whether an insight is actually supported by the data.
* The dashboard requires an internet connection because Plotly JavaScript is loaded from a CDN.

---

# 🚀 Future Improvements

The project can be extended by adding:

* More student records
* Multiple semesters
* Interactive filters
* Department-wise comparisons
* Predictive models
* Student performance prediction
* Automated report generation
* Real college/student data
* Advanced AI-assisted analysis

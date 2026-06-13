# POWERGIT

A dynamic GitHub analytics dashboard built using Python, GitHub REST API, pandas, postgresql and Power BI .

PowerGit transforms raw GitHub repository data into meaningful engineering and collaboration insights through automated data extraction, transformation, and interactive business intelligence dashboards.

---

## 🚀 Project Overview

This project fetches real repository data from the GitHub REST API, processes it using Python and pandas, and visualizes key repository metrics in Power BI.

The goal is to help developers, maintainers, and contributors understand repository activity, contribution patterns, pull request workflows, and issue management through data-driven insights.

### Workflow

```text
GitHub API
     ↓
Python ETL Pipeline
     ↓
Data Cleaning & Transformation
     ↓
SQL Dataset
     ↓
Power BI Dashboards
```

---

## ✨ Features

* GitHub REST API integration
* Automated data extraction using Python
* Data cleaning and transformation with pandas
* PstgreSQL integration
* Dynamic repository switching
* Interactive Power BI dashboards
* Contributor analytics and repository insights
* Pull request and issue workflow analysis
* KPI-based reporting and visual storytelling

---

## 🛠️ Tech Stack

### Data Collection

* Python
* requests
* GitHub REST API

### Data Processing

* pandas
* python-dotenv

### Visualization

* Power BI

### Database

* PostgreSQL
---

## 📂 Datasets Generated

The ETL pipeline generates the following datasets:

| Dataset          | Description                                     |
| ---------------- | ----------------------------------------------- |
| contributors  | Contributor information and contribution counts |
| commits     | Commit history and activity data                |
| prs        | Pull request analytics and merge metrics        |
| issues     | Repository issue tracking data                  |

---

## 📊 Dashboard Pages

### 1. Repository Overview

<img width="608" height="329" alt="Screenshot 2026-06-06 215023" src="https://github.com/user-attachments/assets/7f0f8d86-852d-45ff-8e22-534a74f8b47b" />


Provides a high-level summary of repository health and activity.

**Key Metrics**

* Total Contributors
* Total Commits
* Total Pull Requests
* Total Issues
* Average Merge Time


### 2. Contributor Analytics

<img width="614" height="336" alt="Screenshot 2026-06-06 215034" src="https://github.com/user-attachments/assets/bd6d43d6-41fa-4d43-9c37-5ca02c2b2e01" />

Analyzes contributor behavior and repository participation.

**Visuals**

* Contributor Dominance Analysis
* Contribution Share Distribution
* Commit Activity by Weekday
* Contributor Ranking Table
* Contribution Insights

**Questions Answered**

* Who contributes the most?
* How concentrated are contributions?
* What are the contribution patterns across the week?

---

### 3. PR & Issue Intelligence

<img width="609" height="324" alt="Screenshot 2026-06-06 215100" src="https://github.com/user-attachments/assets/1ffaf585-da78-416d-a78e-f8f3479d3eef" />

Provides workflow and maintenance analytics.

**Visuals**

* Pull Request State Distribution
* Merge Time Analysis
* Pull Request Activity Trends
* Issue State Distribution
* Most Discussed Issues
* PR Details Table

**Questions Answered**

* How efficiently are pull requests processed?
* What is the repository's issue management status?
* Which issues generate the most discussion?

---

## 🔄 Dynamic Repository Refresh

The project can be reused for any public GitHub repository.

Update the repository information:

```python
OWNER = "facebook"
REPO = "react"
```

Run:

```bash
python scripts/fetch_github_data.py
```

Then refresh Power BI to update all dashboards.

---


## 🧠 Skills Demonstrated

* Data Analytics
* PostgreSQL integration
* API Integration
* ETL Pipeline Development
* Data Cleaning & Transformation
* Dashboard Design

---

## 📁 Project Structure

```text
gitlytics/
│
├── scripts/
│   └── fetch_github_data.py
├── powerbi/
│   └── gitlytics_dashboard.pbix
├── .env
├── requirements.txt
└── README.md
```

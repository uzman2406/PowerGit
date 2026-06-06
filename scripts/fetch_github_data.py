import requests
import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

OWNER = os.getenv("OWNER")
REPO = os.getenv("REPO")

BASE_URL = f"https://api.github.com/repos/{OWNER}/{REPO}"

headers = {"Authorization": f"token {GITHUB_TOKEN}"}
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@localhost/powergit")

def fetch_paginated_data(endpoint,max_pages=5,state_all=False):
    all_data = []
    for page in range(1, max_pages + 1):
        params = {
            "page": page,
            "per_page": 100
        }
        if state_all:
            params["state"] = "all"
        url = f"{BASE_URL}/{endpoint}"
        response = requests.get(url,headers=headers,params=params)

        if response.status_code == 200:
            page_data = response.json()
            if not page_data:
                break
            all_data.extend(page_data)
        else:

            print(f"\nError fetching {endpoint}")
            print("Status Code:", response.status_code)
            print("Response:", response.text)
            break

    return all_data

contributors = fetch_paginated_data(endpoint="contributors",max_pages=3)
contributors_data = []
for contributor in contributors:

    contributors_data.append({
        "username": contributor["login"],
        "contributions": contributor["contributions"],
        "profile_url": contributor["html_url"]
    })

contributors_df = pd.DataFrame(contributors_data)
contributors_df.to_sql("contributors",engine ,if_exists="replace",index=False)

prs = fetch_paginated_data(endpoint="pulls",max_pages=5,state_all=True)
prs_data = []

for pr in prs:
    prs_data.append({
        "pr_number": pr["number"],
        "title": pr["title"],
        "state": pr["state"],
        "created_at": pr["created_at"],
        "merged_at": pr["merged_at"],
        "user": pr["user"]["login"]
    })

prs_df = pd.DataFrame(prs_data)
prs_df["created_at"] = pd.to_datetime(prs_df["created_at"],utc=True)
prs_df["merged_at"] = pd.to_datetime(prs_df["merged_at"],utc=True)
prs_df["is_merged"] = prs_df["merged_at"].notnull()
prs_df["merge_time_hours"] = (prs_df["merged_at"] - prs_df["created_at"]).dt.total_seconds() / 3600

prs_df.to_sql("prs",engine,if_exists="replace",index=False)

issues = fetch_paginated_data(endpoint="issues",max_pages=5,state_all=True)
issues_data = []
for issue in issues:
    if "pull_request" not in issue:
        issues_data.append({
            "issue_number": issue["number"],
            "title": issue["title"],
            "state": issue["state"],
            "created_at": issue["created_at"],
            "comments": issue["comments"],
            "user": issue["user"]["login"]
        })
issues_df = pd.DataFrame(issues_data)
issues_df["created_at"] = pd.to_datetime(issues_df["created_at"],utc=True)
issues_df.to_sql("issues",engine,if_exists="replace",index=False)

commits = fetch_paginated_data(endpoint="commits",max_pages=5)
commits_data = []
for commit in commits:

    commits_data.append({
        "sha": commit["sha"],
        "author": commit["commit"]["author"]["name"],
        "date": commit["commit"]["author"]["date"],
        "message": commit["commit"]["message"]
    })

commits_df = pd.DataFrame(commits_data)
commits_df["date"] = pd.to_datetime(
    commits_df["date"],
    utc=True
)

commits_df["year"] = commits_df["date"].dt.year
commits_df["month"] = commits_df["date"].dt.month_name()
commits_df["month_number"] = commits_df["date"].dt.month
commits_df["weekday"] = commits_df["date"].dt.day_name()
commits_df.to_sql("commits",engine,if_exists="replace",index=False)
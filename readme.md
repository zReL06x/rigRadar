# 🎮 RigRadar

RigRadar is a Python-based Gaming Hardware Market Intelligence Platform
designed to track GPU and CPU prices, analyze performance-per-dollar
metrics, monitor availability trends, and support data-driven PC build
decisions.

------------------------------------------------------------------------

## 📌 Project Overview

RigRadar collects and analyzes hardware market data to provide insights
such as:

-   💰 Price comparison and ranking
-   📈 Price trend monitoring
-   🏆 Performance-per-dollar evaluation
-   🏢 Brand dominance analysis
-   🛒 Availability tracking
-   🖥 Budget-based hardware recommendations

This project demonstrates practical skills in web scraping, data
cleaning, analytics, and dashboard development.

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python 3.11.14
-   requests
-   BeautifulSoup4
-   pandas
-   numpy
-   matplotlib
-   seaborn
-   SQLite
-   Streamlit

------------------------------------------------------------------------

## 📂 Project Structure

RigRadar/ │ ├── app/ ├── dashboard/ ├── data/ ├── benchmarks/ ├──
notebooks/ ├── requirements.txt ├── run.py └── README.md

------------------------------------------------------------------------

## 🚀 Features

### 1. Market Scraper

-   Scrapes GPU & CPU prices
-   Tracks stock availability
-   Collects ratings & review counts

### 2. Data Processing

-   Cleans price formats
-   Normalizes brand names
-   Removes duplicates
-   Stores structured data

### 3. Analytics Engine

-   Price comparison
-   Brand analysis
-   Performance-per-dollar ranking
-   Price spike detection

### 4. Interactive Dashboard

-   Visual price trends
-   Value rankings
-   Brand comparisons
-   Budget build recommendations

------------------------------------------------------------------------

## ⚙️ Installation

1.  Clone the repository:

git clone https://github.com/yourusername/RigRadar.git\
cd RigRadar

2.  Create virtual environment:

python -m venv rigradar_env

3.  Activate environment:

Windows:\
rigradar_env`\Scripts`{=tex}`\activate  `{=tex}

Mac/Linux:\
source rigradar_env/bin/activate

4.  Install dependencies:

pip install -r requirements.txt

------------------------------------------------------------------------

## ▶️ Run the Project

Run scraper:

python run.py

Run dashboard:

streamlit run dashboard/app.py

------------------------------------------------------------------------

## 🎯 Project Goals

-   Build a scalable scraping pipeline
-   Develop a structured analytics engine
-   Create a decision-support dashboard
-   Demonstrate end-to-end data workflow

------------------------------------------------------------------------

## 📈 Future Improvements

-   Automated daily scraping scheduler
-   Machine learning price forecasting
-   Alert system for price drops
-   Deployment to cloud platform

------------------------------------------------------------------------

## 📜 License

This project is for educational and portfolio purposes.

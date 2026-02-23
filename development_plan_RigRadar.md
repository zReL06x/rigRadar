# RigRadar Development Plan

## Gaming Hardware Market Intelligence Platform

------------------------------------------------------------------------

## Project Overview

RigRadar is a Python-based market intelligence platform designed to
monitor GPU and CPU pricing trends, analyze performance-per-dollar
metrics, track availability, and provide data-driven PC build
recommendations.

Project Duration: **7 Weeks**\
Methodology: **Phased Iterative Development**\
Environment: **Python 3.11.14 + Streamlit + SQLite**

------------------------------------------------------------------------

# Overall Development Timeline

  --------------------------------------------------------------------------
  Phase       Duration         Focus Area           Deliverable
  ----------- ---------------- -------------------- ------------------------
  Phase 0     Week 0           Environment Setup    Configured project
                                                    workspace

  Phase 1     Week 1           Scraper Development  Functional data scraper

  Phase 2     Week 2           Data Cleaning &      Clean structured dataset
                               Storage              

  Phase 3     Week 3           Core Analytics       Price & brand insights
                               Engine               

  Phase 4     Week 4           Performance          Performance-per-dollar
                               Intelligence         ranking

  Phase 5     Week 5           Trend Monitoring     Historical tracking
                                                    system

  Phase 6     Week 6           Dashboard            Interactive Streamlit
                               Development          dashboard

  Phase 7     Week 7           Optimization &       Production-ready project
                               Portfolio            
  --------------------------------------------------------------------------

------------------------------------------------------------------------

# Phase Breakdown

## Phase 0 -- Environment Setup (Week 0)

Objectives: - Install Python 3.11.14 - Create virtual environment -
Install required dependencies - Set up project directory structure -
Initialize Git repository

Deliverable: - Clean development environment ready for coding

------------------------------------------------------------------------

## Phase 1 -- Scraper Development (Week 1)

Objectives: - Select 5 GPUs and 5 CPUs to track - Identify 2 e-commerce
sources - Implement scraping using requests + BeautifulSoup - Extract: -
Product name - Brand - Price - Availability - Rating - Review count -
Store raw data in CSV

Deliverable: - Working scraper collecting structured product data

Risks: - Website layout changes - Anti-bot protections

------------------------------------------------------------------------

## Phase 2 -- Data Cleaning & Storage (Week 2)

Objectives: - Convert prices to numeric format - Normalize brand names -
Handle missing values - Remove duplicates - Store cleaned data in SQLite
database

Deliverable: - Cleaned dataset ready for analytics

------------------------------------------------------------------------

## Phase 3 -- Core Analytics Engine (Week 3)

Objectives: - Compute average price per brand - Identify price ranking
by product - Generate brand dominance metrics - Visualize summary
insights using matplotlib/seaborn

Deliverable: - Analytical reports and charts

------------------------------------------------------------------------

## Phase 4 -- Performance Intelligence (Week 4)

Objectives: - Integrate benchmark performance dataset - Calculate
performance-per-dollar metric - Rank hardware by value efficiency -
Categorize into budget/mid/high tiers

Deliverable: - Value ranking engine operational

------------------------------------------------------------------------

## Phase 5 -- Trend Monitoring System (Week 5)

Objectives: - Modify scraper to append daily snapshots - Add timestamp
column - Compute: - Daily % price change - Rolling averages - Price
spike detection

Deliverable: - Historical pricing intelligence system

------------------------------------------------------------------------

## Phase 6 -- Dashboard Development (Week 6)

Objectives: - Build Streamlit dashboard - Add: - Product selection
filters - Price trend graphs - Performance ranking charts - Brand
comparison visuals - Implement budget-based recommendation logic

Deliverable: - Interactive decision-support dashboard

------------------------------------------------------------------------

## Phase 7 -- Optimization & Portfolio Preparation (Week 7)

Objectives: - Refactor codebase for modular structure - Write
professional README - Document insights & findings - Add screenshots -
Freeze dependencies (requirements.txt) - Optional deployment to
Streamlit Cloud

Deliverable: - Production-ready portfolio project

------------------------------------------------------------------------

# Final Outcome

RigRadar will function as a market intelligence platform capable of:

-   Automated hardware price monitoring
-   Performance-per-dollar ranking
-   Brand dominance analysis
-   Price volatility tracking
-   Budget-based PC build recommendation

The completed project demonstrates competencies in: - Web scraping -
Data cleaning - Data analysis - Visualization - Dashboard development -
Project structuring

------------------------------------------------------------------------

End of Development Plan

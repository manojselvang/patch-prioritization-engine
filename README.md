# Patch Prioritization Engine

## Overview

The Patch Prioritization Engine is a risk-based vulnerability management solution that helps security teams determine which assets should be patched first and why.

Unlike traditional vulnerability management approaches that focus only on vulnerability severity, this project combines:

- Asset Inventory Data
- Vulnerability Findings
- Firewall Exposure Analysis
- Environment Context
- CIA Classification
- Deterministic Risk Scoring
- AI-Powered Explanations (Ollama + Phi3)

to produce an explainable and auditable patch prioritization process.

---

## Problem Statement

Security teams often face thousands of vulnerabilities across hundreds or thousands of assets.

Traditional approaches typically prioritize:

- CVSS Score
- Vulnerability Severity

This often results in poor prioritization because business context and exposure are ignored.

Example:

Asset A
- Critical CVE
- Production Core Banking System
- Internet Facing

Asset B
- Critical CVE
- SIT Test Server
- No External Exposure

Both vulnerabilities may have the same severity, but Asset A presents significantly higher business risk.

This project addresses that challenge using deterministic risk scoring and contextual analysis.

---

## Key Features

### Asset Correlation

Combines:

- Asset Inventory
- Vulnerability Findings
- Firewall Rules

into a single asset context.

---

### Exposure Analysis

Analyzes firewall rules to identify:

- Number of connections
- Internet-facing systems
- Exposure score

---

### Risk-Based Scoring

Calculates risk scores using:

- Vulnerability Severity
- CIA Classification
- Environment
- Server Category
- Network Exposure

---

### Patch Prioritization

Generates:

- Priority Ranking
- Risk Score
- Risk Breakdown

for every vulnerable asset.

---

### Explainable Scoring

Every score includes a full breakdown.

Example:

```text
Risk Score: 145

Breakdown

Vulnerability      40
CIA                30
Environment        20
Server Category    20
Exposure           35
```

---

### AI-Assisted Analysis

Uses:

- Ollama
- Phi3

to generate:

- Executive Summary
- Technical Analysis
- Business Impact
- Remediation Guidance

AI explains the risk.

AI does not calculate the risk.

---

### Dashboard

Interactive Streamlit dashboard providing:

- Executive Metrics
- Top Patch Priorities
- Asset Details
- Risk Breakdown
- Risk Distribution
- Application Risk Ranking
- AI Analysis

---

### Reporting

Generate:

#### Excel Report

Includes:

- Executive Summary
- Patch Priorities
- Technical Findings
- Risk Breakdown

#### PDF Executive Report

Includes:

- Executive Summary
- Top 10 Patch Priorities
- Risk Breakdown Summary
- Top 5 Detailed Findings

---

# Architecture

```text
Asset Inventory
       +
Vulnerability Data
       +
Firewall Rules
       |
       v
Data Ingestion
       |
       v
Correlation Engine
       |
       v
Exposure Analysis
       |
       v
Risk Scoring Engine
       |
       v
Patch Prioritization
       |
       +-------> Excel Reporting
       |
       +-------> PDF Reporting
       |
       +-------> Streamlit Dashboard
       |
       +-------> AI Explanation (Phi3)
```

---

# Project Structure

```text
patch-prioritization-engine/

├── ai/
│   ├── ai_analysis.py
│   ├── ollama_client.py
│   └── prompt_builder.py
│
├── correlation/
│   ├── asset_context.py
│   ├── attack_path_analysis.py
│   └── exposure_analysis.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── asset_inventory.csv
│   ├── firewall_rules.csv
│   └── vulnerabilities.csv
│
├── ingestion/
│   ├── asset_loader.py
│   ├── firewall_loader.py
│   └── vulnerability_loader.py
│
├── prioritization/
│   └── patch_prioritizer.py
│
├── reporting/
│   ├── excel_export.py
│   ├── executive_report.py
│   ├── pdf_export.py
│   └── technical_report.py
│
├── scoring/
│   ├── risk_engine.py
│   └── scoring_weights.py
│
|── screenshots/
|
├── reports/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Data Sources

## Asset Inventory

Example Fields:

```text
Asset Name
IP Address
Application
Operating System
VLAN
Server Category
Server Type
CIA Severity
```

---

## Vulnerability Findings

Example Fields:

```text
Asset Name
IP Address
CVE
Priority
```

---

## Firewall Rules

Example Fields:

```text
Source
Destination
Service
```

---

# Risk Scoring Methodology

Risk score is calculated using:

| Factor | Example Weight |
|----------|----------|
| Vulnerability Severity | 40 |
| CIA Severity | 30 |
| Environment | 20 |
| Server Category | 25 |
| Exposure | 35 |

Example:

```text
Critical Vulnerability      40
High CIA                    30
Production Environment      20
Application Server          20
Exposure Score              35

Total Risk Score = 145
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/manojselvang/patch-prioritization-engine.git

cd patch-prioritization-engine
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run Dashboard

```bash
streamlit run dashboard/app.py
```

---

# Generate Excel Report

```bash
python -m reporting.excel_export
```

Output:

```text
reports/patch_prioritization_report.xlsx
```

---

# Generate PDF Report

```bash
python -m reporting.pdf_export
```

Output:

```text
reports/executive_report.pdf
```

---

# Run Complete Workflow

```bash
python main.py
```

---

# Technology Stack

- Python
- Pandas
- Streamlit
- ReportLab
- OpenPyXL
- Ollama
- Phi3

---

# Design Principles

- Deterministic risk scoring
- Explainable prioritization
- Risk-driven patch management
- AI used only for explanation
- Auditable scoring model
- Modular architecture

---

# Future Enhancements

- CVSS Integration
- KEV (Known Exploited Vulnerabilities)
- EPSS Scoring
- Asset Relationship Graphs
- Attack Path Visualization
- Historical Trending
- Automated Ticket Creation
- ServiceNow Integration
- Tenable Integration
- Vulnerability Scanner Connectors
- Executive Dashboard Enhancements

---

# Author

Manoj Selvan G
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import streamlit as st
import pandas as pd

from ai.prompt_builder import build_prompt
from ai.ollama_client import query_phi3

from prioritization.patch_prioritizer import (
    prioritize_patches
)

# ==================================================
# Page Config
# ==================================================

st.set_page_config(
    page_title="Patch Prioritization Engine",
    layout="wide"
)

# ==================================================
# Custom Styling
# ==================================================

st.markdown(
    """
    <style>
    .main {
        padding-top: 1rem;
    }

    div[data-testid="metric-container"] {
        border: 1px solid #2E2E2E;
        padding: 15px;
        border-radius: 10px;
        background-color: #111827;
    }

    div[data-testid="metric-container"] label {
        font-size: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==================================================
# Load Data
# ==================================================

findings = prioritize_patches()

df = pd.DataFrame(findings)

# ==================================================
# Sidebar Filters
# ==================================================

st.sidebar.title(
    "Filters"
)

environment_filter = st.sidebar.multiselect(
    "Environment",
    options=df["server_type"].unique(),
    default=df["server_type"].unique()
)

severity_filter = st.sidebar.multiselect(
    "Severity",
    options=df["vulnerability_priority"].unique(),
    default=df["vulnerability_priority"].unique()
)

application_filter = st.sidebar.multiselect(
    "Application",
    options=df["application"].unique(),
    default=df["application"].unique()
)

df = df[
    (df["server_type"].isin(environment_filter))
    &
    (df["vulnerability_priority"].isin(severity_filter))
    &
    (df["application"].isin(application_filter))
]

# ==================================================
# Header
# ==================================================

st.title(
    "Patch Prioritization Engine"
)

st.caption(
    "Security Exposure Management Dashboard"
)

st.markdown("---")

# ==================================================
# KPI Metrics
# ==================================================

critical_count = len(
    df[
        df["vulnerability_priority"] == "Critical"
    ]
)

high_count = len(
    df[
        df["vulnerability_priority"] == "High"
    ]
)

prod_count = len(
    df[
        df["server_type"] == "PROD"
    ]
)

total_assets = len(df)

average_risk = round(
    df["risk_score"].mean(),
    2
)

highest_risk = round(
    df["risk_score"].max(),
    2
)

k1, k2, k3, k4, k5 = st.columns(5)

k1.metric(
    "Assets",
    total_assets
)

k2.metric(
    "Critical",
    critical_count
)

k3.metric(
    "Production",
    prod_count
)

k4.metric(
    "Average Risk",
    average_risk
)

k5.metric(
    "Highest Risk",
    highest_risk
)

# ==================================================
# Executive Summary
# ==================================================

st.header(
    "Executive Risk Summary"
)

left, right = st.columns(2)

with left:

    st.subheader(
        "Top Risk Assets"
    )

    st.dataframe(
        df[
            [
                "asset_name",
                "application",
                "risk_score"
            ]
        ]
        .sort_values(
            by="risk_score",
            ascending=False
        )
        .head(5),
        use_container_width=True,
        hide_index=True
    )

with right:

    st.subheader(
        "Applications Driving Risk"
    )

    app_risk = (
        df.groupby(
            "application"
        )["risk_score"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    st.bar_chart(
        app_risk
    )

# ==================================================
# Risk Analytics
# ==================================================

st.header(
    "Risk Analytics"
)

col1, col2 = st.columns(2)

with col1:

    st.subheader(
        "Risk Score Distribution"
    )

    risk_chart = df[
        [
            "asset_name",
            "risk_score"
        ]
    ].sort_values(
        by="risk_score",
        ascending=False
    )

    st.bar_chart(
        risk_chart.set_index(
            "asset_name"
        )
    )

with col2:

    st.subheader(
        "Severity Distribution"
    )

    severity_df = (
        df["vulnerability_priority"]
        .value_counts()
        .reset_index()
    )

    severity_df.columns = [
        "Severity",
        "Count"
    ]

    st.bar_chart(
        severity_df.set_index(
            "Severity"
        )
    )

# ==================================================
# Environment Distribution
# ==================================================

st.subheader(
    "Environment Distribution"
)

env_df = (
    df["server_type"]
    .value_counts()
    .reset_index()
)

env_df.columns = [
    "Environment",
    "Count"
]

st.dataframe(
    env_df,
    use_container_width=True,
    hide_index=True
)

# ==================================================
# Patch Queue
# ==================================================

st.header(
    "Patch Prioritization Queue"
)

priority_df = df[
    [
        "priority_rank",
        "asset_name",
        "application",
        "server_type",
        "vulnerability_priority",
        "risk_score"
    ]
].sort_values(
    by="priority_rank"
)

st.dataframe(
    priority_df.head(10),
    use_container_width=True,
    hide_index=True
)

# ==================================================
# Asset Investigation
# ==================================================

st.header(
    "Asset Investigation"
)

selected_asset = st.selectbox(
    "Select Asset",
    df["asset_name"]
)

asset = df[
    df["asset_name"]
    == selected_asset
].iloc[0]

left, right = st.columns(2)

with left:

    st.markdown(
        "### Asset Information"
    )

    st.write(
        f"**Asset Name:** {asset['asset_name']}"
    )

    st.write(
        f"**IP Address:** {asset['ip_address']}"
    )

    st.write(
        f"**Application:** {asset['application']}"
    )

    st.write(
        f"**Environment:** {asset['server_type']}"
    )

    st.write(
        f"**Category:** {asset['server_category']}"
    )

with right:

    st.markdown(
        "### Vulnerability Information"
    )

    st.write(
        f"**CIA Severity:** {asset['cia_severity']}"
    )

    st.write(
        f"**CVE:** {asset['cve']}"
    )

    st.write(
        f"**Severity:** {asset['vulnerability_priority']}"
    )

    st.write(
        f"**Risk Score:** {asset['risk_score']}"
    )

# ==================================================
# Risk Breakdown
# ==================================================

st.subheader(
    "Risk Score Breakdown"
)

breakdown_df = pd.DataFrame(
    list(
        asset["risk_breakdown"].items()
    ),
    columns=[
        "Factor",
        "Score"
    ]
)

breakdown_df = breakdown_df.sort_values(
    by="Score",
    ascending=False
)

st.bar_chart(
    breakdown_df.set_index(
        "Factor"
    )
)

# ==================================================
# AI Analysis
# ==================================================

st.header(
    "AI Recommendation Engine"
)

if st.button(
    "Generate AI Analysis"
):

    prompt = build_prompt(
        asset
    )

    with st.spinner(
        "Generating AI analysis..."
    ):

        response = query_phi3(
            prompt
        )

    st.info(
        response
    )

# ==================================================
# Technical Findings
# ==================================================

st.header(
    "Technical Findings"
)

st.dataframe(
    df.sort_values(
        by="risk_score",
        ascending=False
    ),
    use_container_width=True,
    hide_index=True
)
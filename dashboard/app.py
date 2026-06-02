import sys
from pathlib import Path

project_root = Path(__file__).parent.parent

sys.path.append(
    str(project_root)
)

import streamlit as st
import pandas as pd
from ai.prompt_builder import build_prompt
from ai.ollama_client import query_phi3

from prioritization.patch_prioritizer import (
    prioritize_patches
)

st.set_page_config(
    page_title="Patch Prioritization Engine",
    layout="wide"
)

# ==========================================
# Load Findings
# ==========================================

findings = prioritize_patches()

df = pd.DataFrame(findings)

# ==========================================
# Header
# ==========================================

st.title(
    "Patch Prioritization Engine"
)

st.markdown(
    "Risk-Based Patch Prioritization Dashboard"
)

# ==========================================
# Executive Metrics
# ==========================================

critical_count = len(
    df[
        df["vulnerability_priority"]
        == "Critical"
    ]
)

high_count = len(
    df[
        df["vulnerability_priority"]
        == "High"
    ]
)

prod_count = len(
    df[
        df["server_type"]
        == "PROD"
    ]
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Critical Vulnerabilities",
    critical_count
)

col2.metric(
    "High Vulnerabilities",
    high_count
)

col3.metric(
    "Production Assets",
    prod_count
)

# ==========================================
# Risk Distribution
# ==========================================

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

# ==========================================
# Environment Distribution
# ==========================================

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
    use_container_width=True
)

# ==========================================
# Vulnerability Distribution
# ==========================================

st.subheader(
    "Vulnerability Severity Distribution"
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

# ==========================================
# Applications Driving Risk
# ==========================================

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

# ==========================================
# Top 10 Priorities
# ==========================================

st.subheader(
    "Top 10 Patch Priorities"
)

st.dataframe(

    df[
        [
            "priority_rank",
            "asset_name",
            "application",
            "server_type",
            "vulnerability_priority",
            "risk_score"
        ]
    ].head(10),

    use_container_width=True
)

# ==========================================
# Full Findings
# ==========================================

st.subheader(
    "All Findings"
)

st.dataframe(
    df,
    use_container_width=True
)

# ==========================================
# Asset Details
# ==========================================

st.subheader(
    "Asset Detail"
)

selected_asset = st.selectbox(

    "Select Asset",

    df["asset_name"]
)

asset = df[
    df["asset_name"]
    == selected_asset
].iloc[0]

st.markdown("---")

left, right = st.columns(2)

with left:

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

    st.write(
        f"**CIA Severity:** {asset['cia_severity']}"
    )

    st.write(
        f"**CVE:** {asset['cve']}"
    )

    st.write(
        f"**Vulnerability:** "
        f"{asset['vulnerability_priority']}"
    )

    st.write(
        f"**Risk Score:** "
        f"{asset['risk_score']}"
    )

# ==========================================
# Risk Breakdown
# ==========================================

st.subheader(
    "Risk Score Breakdown"
)

risk_breakdown = asset[
    "risk_breakdown"
]

breakdown_df = pd.DataFrame(

    list(
        risk_breakdown.items()
    ),

    columns=[
        "Factor",
        "Score"
    ]
)

st.bar_chart(

    breakdown_df.set_index(
        "Factor"
    )
)

# ==========================================
# AI Analysis
# ==========================================

st.subheader(
    "AI Risk Analysis"
)

if st.button(
    "Generate AI Analysis"
):

    prompt = build_prompt(
        asset
    )

    with st.spinner(
        "Generating analysis..."
    ):

        response = query_phi3(
            prompt
        )

    st.write(
        response
    )
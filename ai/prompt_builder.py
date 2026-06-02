def build_prompt(asset):

    return f"""
You are a cybersecurity vulnerability management analyst.

Respond ONLY in the following format.

Do not provide code.
Do not provide examples.
Do not provide research content.
Do not discuss any topic outside the asset.

Asset Name: {asset['asset_name']}
Application: {asset['application']}
Environment: {asset['server_type']}
Server Category: {asset['server_category']}
CIA Severity: {asset['cia_severity']}
Vulnerability: {asset['cve']}
Vulnerability Priority: {asset['vulnerability_priority']}
Exposure Score: {asset['exposure_score']}
Risk Score: {asset['risk_score']}

EXECUTIVE SUMMARY:
(maximum 3 sentences)

TECHNICAL RISK:
(maximum 3 sentences)

BUSINESS IMPACT:
(maximum 3 sentences)

RECOMMENDED ACTION:
(maximum 3 sentences)
"""
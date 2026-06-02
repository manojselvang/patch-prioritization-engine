from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from prioritization.patch_prioritizer import (
    prioritize_patches
)


def export_pdf():

    findings = prioritize_patches()

    output_file = (
        "reports/executive_report.pdf"
    )

    doc = SimpleDocTemplate(
        output_file
    )

    styles = getSampleStyleSheet()

    elements = []

    # ==================================================
    # Executive Summary
    # ==================================================

    total_assets = len(findings)

    highest_score = max(
        x["risk_score"]
        for x in findings
    )

    average_score = round(
        sum(
            x["risk_score"]
            for x in findings
        ) / len(findings),
        2
    )

    top_asset = findings[0]

    elements.append(
        Paragraph(
            "Patch Prioritization Executive Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "Executive Summary",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Assets Reviewed: {total_assets}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Highest Risk Score: {highest_score}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Average Risk Score: {average_score}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Highest Risk Asset: {top_asset['asset_name']}",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # ==================================================
    # Top 10 Priorities
    # ==================================================

    elements.append(
        Paragraph(
            "Top 10 Patch Priorities",
            styles["Heading1"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    for finding in findings[:10]:

        text = f"""
        Rank: {finding['priority_rank']}<br/>
        Asset: {finding['asset_name']}<br/>
        Application: {finding['application']}<br/>
        Environment: {finding['server_type']}<br/>
        Risk Score: {finding['risk_score']}
        """

        elements.append(
            Paragraph(
                text,
                styles["Normal"]
            )
        )

        elements.append(
            Spacer(1, 10)
        )

    elements.append(
        PageBreak()
    )

    # ==================================================
    # Risk Breakdown Summary
    # ==================================================

    elements.append(
        Paragraph(
            "Risk Breakdown Summary",
            styles["Heading1"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    for finding in findings[:10]:

        breakdown = finding[
            "risk_breakdown"
        ]

        text = f"""
        <b>{finding['asset_name']}</b><br/>

        Risk Score:
        {finding['risk_score']}<br/>

        Vulnerability:
        {breakdown['vulnerability']}<br/>

        CIA:
        {breakdown['cia']}<br/>

        Environment:
        {breakdown['environment']}<br/>

        Server Category:
        {breakdown['server_category']}<br/>

        Exposure:
        {breakdown['exposure']}<br/>
        """

        elements.append(
            Paragraph(
                text,
                styles["Normal"]
            )
        )

        elements.append(
            Spacer(1, 10)
        )

    elements.append(
        PageBreak()
    )

    # ==================================================
    # Top 5 Detailed Findings
    # ==================================================

    elements.append(
        Paragraph(
            "Top 5 Detailed Findings",
            styles["Heading1"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    for finding in findings[:5]:

        breakdown = finding[
            "risk_breakdown"
        ]

        text = f"""
        <b>Priority Rank:
        {finding['priority_rank']}</b><br/><br/>

        Asset Name:
        {finding['asset_name']}<br/>

        IP Address:
        {finding['ip_address']}<br/>

        Application:
        {finding['application']}<br/>

        Environment:
        {finding['server_type']}<br/>

        Server Category:
        {finding['server_category']}<br/>

        CIA Severity:
        {finding['cia_severity']}<br/>

        CVE:
        {finding['cve']}<br/>

        Vulnerability Priority:
        {finding['vulnerability_priority']}<br/>

        Connection Count:
        {finding['connection_count']}<br/>

        Exposure Score:
        {finding['exposure_score']}<br/>

        Risk Score:
        {finding['risk_score']}<br/><br/>

        Risk Breakdown<br/>

        Vulnerability:
        {breakdown['vulnerability']}<br/>

        CIA:
        {breakdown['cia']}<br/>

        Environment:
        {breakdown['environment']}<br/>

        Server Category:
        {breakdown['server_category']}<br/>

        Exposure:
        {breakdown['exposure']}<br/>
        """

        elements.append(
            Paragraph(
                text,
                styles["Normal"]
            )
        )

        elements.append(
            Spacer(1, 15)
        )

    doc.build(
        elements
    )

    print(
        f"\nPDF Report generated: {output_file}"
    )

    return output_file


if __name__ == "__main__":

    export_pdf()
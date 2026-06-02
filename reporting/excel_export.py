import pandas as pd

from prioritization.patch_prioritizer import (
    prioritize_patches
)


def export_to_excel():

    findings = prioritize_patches()

    output_file = (
        "reports/patch_prioritization_report.xlsx"
    )

    # ==================================================
    # Sheet 1 - Executive Summary
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

    top_asset = findings[0]["asset_name"]

    top_application = findings[0]["application"]

    executive_data = [

        ["Metric", "Value"],

        ["Total Assets", total_assets],

        ["Highest Risk Score", highest_score],

        ["Average Risk Score", average_score],

        ["Highest Risk Asset", top_asset],

        ["Highest Risk Application", top_application]
    ]

    executive_df = pd.DataFrame(
        executive_data
    )

    # ==================================================
    # Sheet 2 - Patch Priorities
    # ==================================================

    priority_rows = []

    for finding in findings:

        priority_rows.append({

            "Priority Rank":
                finding["priority_rank"],

            "Asset Name":
                finding["asset_name"],

            "IP Address":
                finding["ip_address"],

            "Application":
                finding["application"],

            "Environment":
                finding["server_type"],

            "Server Category":
                finding["server_category"],

            "CIA Severity":
                finding["cia_severity"],

            "CVE":
                finding["cve"],

            "Vulnerability Priority":
                finding["vulnerability_priority"],

            "Risk Score":
                finding["risk_score"]
        })

    priorities_df = pd.DataFrame(
        priority_rows
    )

    # ==================================================
    # Sheet 3 - Technical Findings
    # ==================================================

    technical_rows = []

    for finding in findings:

        technical_rows.append({

            "Priority Rank":
                finding["priority_rank"],

            "Asset Name":
                finding["asset_name"],

            "IP Address":
                finding["ip_address"],

            "Application":
                finding["application"],

            "Operating System":
                finding["operating_system"],

            "VLAN":
                finding["vlan"],

            "Environment":
                finding["server_type"],

            "Server Category":
                finding["server_category"],

            "CIA Severity":
                finding["cia_severity"],

            "CVE":
                finding["cve"],

            "Vulnerability Priority":
                finding["vulnerability_priority"],

            "Connection Count":
                finding["connection_count"],

            "Internet Facing":
                finding["internet_facing"],

            "Exposure Score":
                finding["exposure_score"],

            "Risk Score":
                finding["risk_score"]
        })

    technical_df = pd.DataFrame(
        technical_rows
    )

    # ==================================================
    # Sheet 4 - Risk Breakdown
    # ==================================================

    breakdown_rows = []

    for finding in findings:

        breakdown_rows.append({

            "Asset Name":
                finding["asset_name"],

            "Risk Score":
                finding["risk_score"],

            "Vulnerability Score":
                finding["risk_breakdown"]["vulnerability"],

            "CIA Score":
                finding["risk_breakdown"]["cia"],

            "Environment Score":
                finding["risk_breakdown"]["environment"],

            "Server Category Score":
                finding["risk_breakdown"]["server_category"],

            "Exposure Score":
                finding["risk_breakdown"]["exposure"]
        })

    breakdown_df = pd.DataFrame(
        breakdown_rows
    )

    # ==================================================
    # Write Workbook
    # ==================================================

    with pd.ExcelWriter(
        output_file,
        engine="openpyxl"
    ) as writer:

        executive_df.to_excel(
            writer,
            sheet_name="Executive Summary",
            index=False,
            header=False
        )

        priorities_df.to_excel(
            writer,
            sheet_name="Patch Priorities",
            index=False
        )

        technical_df.to_excel(
            writer,
            sheet_name="Technical Findings",
            index=False
        )

        breakdown_df.to_excel(
            writer,
            sheet_name="Risk Breakdown",
            index=False
        )

    print(
        f"\nExcel report generated: {output_file}"
    )

    return output_file


if __name__ == "__main__":

    export_to_excel()
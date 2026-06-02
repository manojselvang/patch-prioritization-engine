from prioritization.patch_prioritizer import (
    prioritize_patches
)


def generate_executive_report():

    findings = prioritize_patches()

    total_assets = len(findings)

    critical_assets = len(
        [
            x for x in findings
            if x["vulnerability_priority"] == "Critical"
        ]
    )

    high_assets = len(
        [
            x for x in findings
            if x["vulnerability_priority"] == "High"
        ]
    )

    prod_assets = len(
        [
            x for x in findings
            if x["server_type"] == "PROD"
        ]
    )

    uat_assets = len(
        [
            x for x in findings
            if x["server_type"] == "UAT"
        ]
    )

    sit_assets = len(
        [
            x for x in findings
            if x["server_type"] == "SIT"
        ]
    )

    print("=" * 80)
    print("EXECUTIVE RISK SUMMARY")
    print("=" * 80)

    print()

    print(f"Total Vulnerable Assets : {total_assets}")
    print(f"Critical Vulnerabilities: {critical_assets}")
    print(f"High Vulnerabilities    : {high_assets}")

    print()

    print("ENVIRONMENT BREAKDOWN")

    print(f"PROD Assets : {prod_assets}")
    print(f"UAT Assets  : {uat_assets}")
    print(f"SIT Assets  : {sit_assets}")

    print()

    print("=" * 80)
    print("TOP 10 PATCH PRIORITIES")
    print("=" * 80)

    print()

    for finding in findings[:10]:

        print(
            f"#{finding['priority_rank']:<3}"
            f"{finding['asset_name']:<25}"
            f"Score: {finding['risk_score']}"
        )

    print()

    print("=" * 80)
    print("IMMEDIATE PATCH RECOMMENDATIONS")
    print("=" * 80)

    print()

    for finding in findings[:5]:

        print(
            f"{finding['asset_name']} "
            f"({finding['application']})"
        )

    print()

    print("=" * 80)


if __name__ == "__main__":

    generate_executive_report()
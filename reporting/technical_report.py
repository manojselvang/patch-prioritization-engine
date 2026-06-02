from prioritization.patch_prioritizer import (
    prioritize_patches
)


def generate_technical_report():

    findings = prioritize_patches()

    for finding in findings:

        print("=" * 80)

        print(
            f"PATCH PRIORITY #{finding['priority_rank']}"
        )

        print()

        print(
            f"Asset Name       : {finding['asset_name']}"
        )

        print(
            f"IP Address       : {finding['ip_address']}"
        )

        print(
            f"Application      : {finding['application']}"
        )

        print(
            f"Environment      : {finding['server_type']}"
        )

        print(
            f"Server Category  : {finding['server_category']}"
        )

        print(
            f"CIA Severity     : {finding['cia_severity']}"
        )

        print(
            f"CVE              : {finding['cve']}"
        )

        print(
            f"Vulnerability    : "
            f"{finding['vulnerability_priority']}"
        )

        print(
            f"Exposure Score   : "
            f"{finding['exposure_score']}"
        )

        print(
            f"Risk Score       : "
            f"{finding['risk_score']}"
        )

        print()

        print("RISK SCORE BREAKDOWN")

        for factor, score in (
            finding["risk_breakdown"].items()
        ):

            print(
                f"{factor:<20} {score}"
            )

        print()

        print(
            f"{'TOTAL':<20} "
            f"{finding['risk_score']}"
        )

        print("=" * 80)

        print()


if __name__ == "__main__":

    generate_technical_report()
from correlation.asset_context import build_asset_context

from scoring.scoring_weights import (
    VULNERABILITY_WEIGHTS,
    CIA_WEIGHTS,
    ENVIRONMENT_WEIGHTS,
    SERVER_CATEGORY_WEIGHTS
)


def calculate_risk_scores():

    assets = build_asset_context()

    findings = []

    for asset in assets:

        vulnerability_score = (
            VULNERABILITY_WEIGHTS.get(
                asset["vulnerability_priority"],
                0
            )
        )

        cia_score = (
            CIA_WEIGHTS.get(
                asset["cia_severity"],
                0
            )
        )

        environment_score = (
            ENVIRONMENT_WEIGHTS.get(
                asset["server_type"],
                0
            )
        )

        category_score = (
            SERVER_CATEGORY_WEIGHTS.get(
                asset["server_category"],
                0
            )
        )

        exposure_score = (
            asset["exposure_score"]
        )

        total_score = (

            vulnerability_score

            + cia_score

            + environment_score

            + category_score

            + exposure_score
        )

        asset["risk_breakdown"] = {
        "vulnerability": vulnerability_score,
        "cia": cia_score,
        "environment": environment_score,
        "server_category": category_score,
        "exposure": exposure_score
    }

        asset["risk_score"] = total_score

        findings.append(asset)

    return findings


if __name__ == "__main__":

    findings = calculate_risk_scores()

    for finding in findings:

        print(
            finding["asset_name"],
            finding["risk_score"]
        )
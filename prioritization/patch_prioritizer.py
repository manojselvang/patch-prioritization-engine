from scoring.risk_engine import calculate_risk_scores


def prioritize_patches():

    findings = calculate_risk_scores()

    findings = sorted(
        findings,
        key=lambda x: x["risk_score"],
        reverse=True
    )

    for rank, finding in enumerate(
        findings,
        start=1
    ):

        finding["priority_rank"] = rank

    return findings


if __name__ == "__main__":

    findings = prioritize_patches()

    print("\nPATCH PRIORITY LIST\n")

    for finding in findings:

        print(
            f"#{finding['priority_rank']} "
            f"{finding['asset_name']} "
            f"({finding['risk_score']})"
        )
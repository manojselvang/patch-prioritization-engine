from prioritization.patch_prioritizer import (
    prioritize_patches
)

from reporting.executive_report import (
    generate_executive_report
)

from reporting.technical_report import (
    generate_technical_report
)

from ai.prompt_builder import (
    build_prompt
)

from ai.ollama_client import (
    query_phi3
)


def generate_ai_findings(findings, top_n=5):

    print("=" * 80)
    print("AI ANALYSIS")
    print("=" * 80)

    for asset in findings[:top_n]:

        print("\n")
        print("=" * 80)

        print(
            f"PATCH PRIORITY #{asset['priority_rank']}"
        )

        print(
            f"ASSET : {asset['asset_name']}"
        )

        print("=" * 80)

        prompt = build_prompt(asset)

        response = query_phi3(prompt)

        print(response)

        print("\n")


def main():

    findings = prioritize_patches()

    generate_executive_report()

    print("\n\n")

    generate_technical_report()

    print("\n\n")

    generate_ai_findings(
        findings,
        top_n=5
    )


if __name__ == "__main__":

    main()
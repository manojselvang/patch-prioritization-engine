from prioritization.patch_prioritizer import (
    prioritize_patches
)

from ai.prompt_builder import (
    build_prompt
)

from ai.ollama_client import (
    query_phi3
)


def generate_ai_analysis():

    findings = prioritize_patches()

    top_asset = findings[0]

    prompt = build_prompt(
        top_asset
    )

    response = query_phi3(
        prompt
    )

    print(response)


if __name__ == "__main__":

    generate_ai_analysis()
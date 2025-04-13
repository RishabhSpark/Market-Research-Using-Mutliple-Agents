import argparse
from agents.agents_pipeline import agents_pipeline


def run_cli() -> None:
    parser = argparse.ArgumentParser(description="Run the AI Use Case Agent Pipeline.")
    parser.add_argument(
        "company_or_industry",
        type=str,
        help="The industry or company to research (e.g., 'Tesla')",
    )

    args = parser.parse_args()

    print("Running full pipeline for:", args.company_or_industry)
    results = agents_pipeline(args.company_or_industry)

    print("\n Industry Research")
    print("-" * 80)
    print(results["summary"])

    print("\n AI/ML Use Cases")
    print("-" * 80)
    print(results["usecases"])

    print("\n Dataset Search Links (Kaggle & HuggingFace)")
    print("-" * 80)
    print(results["datasets"])

    print("\n Suggested GenAI Tools")
    print("-" * 80)
    print(results["genai_tools"])
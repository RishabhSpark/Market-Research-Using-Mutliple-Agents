# main.py

from agents.agents_pipeline import agents_pipeline
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Run the AI Use Case Agent Pipeline.")
    parser.add_argument(
        "industry",
        type=str,
        help="The industry or company to research (e.g., 'Healthcare', 'Retail', 'Infosys')",
    )

    args = parser.parse_args()

    try:
        print("Running full pipeline for:", args.industry)
        results = agents_pipeline(args.industry)

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

    except Exception as e:
        print("\nAn error occurred while running the pipeline.")
        print(str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
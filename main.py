import sys
from cli import run_cli

def main():
    try:
        run_cli()
    except Exception as e:
        print("\n An error occurred while running the pipeline.")
        print(str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
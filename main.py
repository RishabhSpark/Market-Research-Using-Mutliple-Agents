from agents.run_agents import run_agents
# if __name__ == "__main__":
#     company = input("Enter a company or industry to research: ")
#     result = research_industry(company)
#     print("\n--- Industry Research Output ---\n")
#     print(result)


if __name__ == "__main__":
    company_name = input("Enter a company or industry to research: ")

    # Run both agents with the inputs
    run_agents(company_name)
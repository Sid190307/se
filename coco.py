
def cocomo_estimation(kloc, project_type, cost_per_pm=10000):

    # COCOMO coefficients
    cocomo_coefficients = {
        'organic': (2.4, 1.05, 2.5, 0.38),
        'semi-detached': (3.0, 1.12, 2.5, 0.35),
        'embedded': (3.6, 1.20, 2.5, 0.32)
    }

    # Validate project type
    if project_type.lower() not in cocomo_coefficients:
        raise ValueError(
            "Invalid project type. Choose from: organic, semi-detached, embedded."
        )

    a, b, c, d = cocomo_coefficients[project_type.lower()]

    # Calculate Effort
    effort = a * (kloc ** b)

    # Calculate Development Time
    dev_time = c * (effort ** d)

    # Calculate Average Staff Size
    avg_staff_size = effort / dev_time

    # Calculate Productivity
    productivity = kloc / effort

    # Calculate Cost Estimation
    cost = effort * cost_per_pm

    # Return all results in a dictionary
    return {
        "Effort (person-months)": round(effort, 2),
        "Development Time (months)": round(dev_time, 2),
        "Average Staff Size": round(avg_staff_size, 2),
        "Productivity (KLOC/person-month)": round(productivity, 2),
        "Estimated Cost (USD)": round(cost, 2)
    }


# Example usage
if __name__ == "__main__":

    kloc = float(input("Enter the number of lines of code (in KLOC): "))

    project_type = input(
        "Enter the type of project (organic / semi-detached / embedded): "
    )

    result = cocomo_estimation(kloc, project_type)

    print("\n--- Estimation Results ---")

    for key, value in result.items():
        print(f"{key}: {value}")

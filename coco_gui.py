
import tkinter as tk
from tkinter import messagebox


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

    # Calculate effort
    effort = a * (kloc ** b)

    # Calculate development time
    dev_time = c * (effort ** d)

    # Calculate average staff size
    avg_staff_size = effort / dev_time

    # Calculate productivity
    productivity = kloc / effort

    # Calculate cost
    cost = effort * cost_per_pm

    return {
        "Effort (person-months)": round(effort, 2),
        "Development Time (months)": round(dev_time, 2),
        "Average Staff Size": round(avg_staff_size, 2),
        "Productivity (KLOC/person-month)": round(productivity, 2),
        "Estimated Cost (USD)": round(cost, 2)
    }


# GUI Function
def estimate():
    try:
        kloc = float(entry_kloc.get())
        project_type = project_type_var.get()

        if kloc <= 0:
            messagebox.showerror("Input Error", "KLOC must be greater than zero.")
            return

        if not project_type:
            messagebox.showerror("Error", "Please select a project type.")
            return

        result = cocomo_estimation(kloc, project_type)

        output_text.delete("1.0", tk.END)

        for key, value in result.items():
            output_text.insert(tk.END, f"{key}: {value}\n")

    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))


# Create main window
root = tk.Tk()
root.title("COCOMO Cost & Time Estimator")

# KLOC input
tk.Label(
    root, text="Enter KLOC (1000 lines of code):"
).grid(row=0, column=0, pady=10)

entry_kloc = tk.Entry(root)
entry_kloc.grid(row=0, column=1)

# Project type selection
tk.Label(root, text="Select Project Type").grid(
    row=1, column=0, pady=10
)

project_type_var = tk.StringVar()

tk.Radiobutton(
    root, text="Organic",
    variable=project_type_var, value="organic"
).grid(row=2, column=0, pady=10, sticky="w")

tk.Radiobutton(
    root, text="Semi-detached",
    variable=project_type_var, value="semi-detached"
).grid(row=3, column=0, pady=10, sticky="w")

tk.Radiobutton(
    root, text="Embedded",
    variable=project_type_var, value="embedded"
).grid(row=4, column=0, pady=10, sticky="w")

# Estimate button
tk.Button(
    root, text="Estimate", command=estimate, bg="lightgreen"
).grid(row=5, column=0, columnspan=2, pady=10)

# Output area
output_text = tk.Text(root, height=10, width=50)
output_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Run application
root.mainloop()

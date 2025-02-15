import os
import pandas as pd
from src.helper_tes import SecretSanta

def main():
    employees_file = "data/employees.csv"
    previous_year_file = "data/previous_year.csv"
    output_file = "output/secret_santa_assignments.csv"

    employees = SecretSanta.load_csv(employees_file)
    if employees is None or employees.empty:
        return

    employees = employees.to_dict(orient="records")

    previous_year_data = SecretSanta.load_csv(previous_year_file)
    previous_year = {row['Employee_Name']: row['Secret_Child_Name'] for _, row in previous_year_data.iterrows()} if previous_year_data is not None and not previous_year_data.empty else {}

    for _ in range(10):  
        assignments = SecretSanta.generate_secret_santa(employees, previous_year)
        if assignments is not None:
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            SecretSanta.save_csv(pd.DataFrame(assignments), output_file)
            return

if __name__ == "__main__":
    main()

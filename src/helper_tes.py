import pandas as pd
import random
import copy

class SecretSanta:
    @staticmethod
    def load_csv(file_path):
        "load CSV file"
        try:
            return pd.read_csv(file_path)
        except (FileNotFoundError, Exception):
            return None

    @staticmethod
    def save_csv(df, file_path):
        "save csv"
        try:
            df.to_csv(file_path, index=False)
        except Exception:
            pass

    @staticmethod
    def generate_secret_santa(employees, previous_year):
        "Generates Secret Santa assignments"
        givers = copy.deepcopy(employees)
        receivers = copy.deepcopy(employees)

        for _ in range(100):  
            random.shuffle(receivers)

            assignments = [
                {
                    "Employee_Name": giver["Employee_Name"],
                    "Employee_EmailID": giver["Employee_EmailID"],
                    "Secret_Child_Name": receiver["Employee_Name"],
                    "Secret_Child_EmailID": receiver["Employee_EmailID"]
                }
                for giver, receiver in zip(givers, receivers)
                if giver["Employee_Name"] != receiver["Employee_Name"]
                and previous_year.get(giver["Employee_Name"]) != receiver["Employee_Name"]
            ]

            if len(assignments) == len(givers):
                return assignments
        return None 
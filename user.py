# user.py

class User:
    def __init__(self, age, gender, income, expenses):
        self.age = age
        self.gender = gender
        self.income = income
        self.expenses = expenses

    def to_dict(self):
        # Prepare the dictionary format for CSV writing
        return {
            "age": self.age,
            "gender": self.gender,
            "income": self.income,
            "utilities": self.expenses.get("utilities", 0),
            "entertainment": self.expenses.get("entertainment", 0),
            "school_fees": self.expenses.get("school_fees", 0),
            "shopping": self.expenses.get("shopping", 0),
            "healthcare": self.expenses.get("healthcare", 0),
        }

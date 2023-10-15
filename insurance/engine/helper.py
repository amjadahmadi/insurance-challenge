import datetime


def map_category(value):
    if value <= 0:
        return "economic"
    elif value <= 2:
        return "regular"
    return "responsible"


class Insurance:
    def __init__(self, age: int, dependents: int, house: dict | None, income: int, marital_status: str,
                 risk_questions: list, vehicle: dict | None):
        self.age = age
        self.dependents = dependents
        self.house = house
        self.income = income
        self.marital_status = marital_status
        self.vehicle = vehicle
        self.base_score = sum(risk_questions)

    def calculate_age(self):
        # age affects on all insurance
        age_score = 0
        if self.age < 30:
            age_score = -2
        elif 30 <= self.age < 40:
            age_score = -1
        return age_score

    def calculate_income(self):
        # income affects on all insurance
        income_score = 0
        if self.income >= 200_000:
            income_score = -1
        return income_score

    def calculate_home(self):
        return 1 if self.house and self.house['ownership_status'] == 'mortgaged' else 0

    def calculate_dependents(self):
        return 1 if self.dependents > 0 else 0


# we can use ABC class also

# first, we check the ineligibility

class HomeInsurance:
    def __init__(self, insurance: Insurance):
        self.insurance = insurance

    def check_ineligible(self):
        return False if self.insurance.house else True

    def total_score(self):
        if self.check_ineligible():
            return "ineligible"
        age_score = self.insurance.calculate_age()
        income_score = self.insurance.calculate_income()
        home_score = self.insurance.calculate_home()
        return map_category(age_score + income_score + home_score + self.insurance.base_score)


class DisabilityInsurance:
    def __init__(self, insurance: Insurance):
        self.insurance = insurance

    def check_ineligible(self):
        return False if (self.insurance.age < 60 and self.insurance.income) else True

    def total_score(self):
        if self.check_ineligible():
            return "ineligible"
        age_score = self.insurance.calculate_age()
        income_score = self.insurance.calculate_income()
        home_score = self.insurance.calculate_home()
        dependents_score = self.insurance.calculate_dependents()
        marital_score = -1 if self.insurance.marital_status == 'married' else 0
        return map_category(
            age_score + income_score + home_score + dependents_score + marital_score + self.insurance.base_score)


class AutoInsurance:
    def __init__(self, insurance: Insurance):
        self.insurance = insurance

    def check_ineligible(self):
        return False if self.insurance.vehicle else True

    def total_score(self):
        if self.check_ineligible():
            return "ineligible"
        age_score = self.insurance.calculate_age()
        income_score = self.insurance.calculate_income()
        auto_score = 1 if datetime.datetime.now().year - self.insurance.vehicle['year'] <= 5 else 0
        return map_category(age_score + income_score + auto_score + self.insurance.base_score)


class LifeInsurance:
    def __init__(self, insurance: Insurance):
        self.insurance = insurance

    def check_ineligible(self):
        return False if self.insurance.age < 60 else True

    def total_score(self):
        if self.check_ineligible():
            return "ineligible"
        age_score = self.insurance.calculate_age()
        income_score = self.insurance.calculate_income()
        dependents_score = self.insurance.calculate_dependents()
        marital_score = 1 if self.insurance.marital_status == 'marital_status' else 0
        return map_category(age_score + income_score + dependents_score + marital_score + self.insurance.base_score)


def calculate_all_insurance(kwargs):
    # crate base information
    base_insurance = Insurance(**kwargs)
    return {
        "auto": AutoInsurance(base_insurance).total_score(),
        "disability": DisabilityInsurance(base_insurance).total_score(),
        "home": HomeInsurance(base_insurance).total_score(),
        "life": LifeInsurance(base_insurance).total_score()
    }

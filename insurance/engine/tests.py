from django.test import TestCase, RequestFactory
from .views import UserInsuranceView
from .helper import *


class SimpleTest(TestCase):
    def setUp(self):

        self.insurance = {
            "age": 35,
            "dependents": 2,
            "house": None,
            "income": 0,
            "marital_status": "married",
            "risk_questions": [0, 1, 0],
            "vehicle": {"year": 2018}
        }

    def test_details(self):
        print(calculate_all_insurance(self.insurance))

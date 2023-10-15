from django.test import TestCase
from .helper import *


class SimpleTest(TestCase):
    def setUp(self):
        self.insurance1 = {
            "age": 70,
            "dependents": 2,
            "house": {"ownership_status": "owned"},
            "income": 0,
            "marital_status": "married",
            "risk_questions": [1, 1, 1],
            "vehicle": {"year": 2018}
        }
        self.insurance2 = {
            "age": 35,
            "dependents": 2,
            "house": {"ownership_status": "mortgaged"},
            "income": 100000,
            "marital_status": "married",
            "risk_questions": [0, 1, 0],
            "vehicle": {"year": 2018}
        }
        self.insurance3 = {
            "age": 20,
            "dependents": 0,
            "house": None,
            "income": 250000,
            "marital_status": "single",
            "risk_questions": [0, 0, 0],
            "vehicle": {"year": 2020}
        }
        self.insurance4 = {
            "age": 45,
            "dependents": 3,
            "house": None,
            "income": 100000,
            "marital_status": "married",
            "risk_questions": [1, 1, 0],
            "vehicle": None
        }

    def test_details(self):
        self.assertEqual(calculate_all_insurance(self.insurance1)['auto'], 'responsible')
        self.assertEqual(calculate_all_insurance(self.insurance2)['home'], 'regular')
        self.assertEqual(calculate_all_insurance(self.insurance3)['life'], 'economic')
        self.assertEqual(calculate_all_insurance(self.insurance4)['auto'], 'ineligible')
        self.assertEqual(calculate_all_insurance(self.insurance4)['disability'], 'regular')
        self.assertEqual(calculate_all_insurance(self.insurance4)['life'], 'responsible')

"""Economy courses"""
from src.builder import ONTOLOGY
from src.construction.micro_learning.classes import Course
from src.instances.micro_learning.thematics import economy

with ONTOLOGY:
    numeric_economy = Course("NumericEconomy")
    currency_and_financial_institutions = Course("Currency_and_financial_instituations")
    poverties_and_inequialities = Course("Poverty and inequalities")
    macroeconomy = Course("Macroeconomy")

    economy_courses = [
        macroeconomy,
        numeric_economy,
        currency_and_financial_institutions,
        poverties_and_inequialities,
    ]

    economy.has_as_course.extend(economy_courses)

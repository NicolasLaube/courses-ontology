"""Economy courses"""
from src.builder import ONTOLOGY
from src.construction.micro_learning.micro_learning_classes import Course
from src.instances.micro_learning.thematics import economy

with ONTOLOGY:
    micro_economics = Course("Microeconomics")

    numeric_economy = Course("NumericEconomy")
    currency_and_financial_institutions = Course("CurrencyAndFinancialInstituations")
    poverties_and_inequialities = Course("PovertyAndInequalities")
    macroeconomy = Course("Macroeconomy")

    economy_courses = [
        macroeconomy,
        numeric_economy,
        currency_and_financial_institutions,
        poverties_and_inequialities,
    ]

    economy.has_as_course.extend(economy_courses)

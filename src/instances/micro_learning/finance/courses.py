"""Finance courses"""
from src.builder import ONTOLOGY
from src.construction.micro_learning.classes import Course
from src.instances.micro_learning.thematics import finance

with ONTOLOGY:
    business_finance = Course("BusinessFinance")
    market_finance = Course("MarketFinance")
    insurance = Course("Insurance")

    finance_courses = [business_finance, market_finance, insurance]

    finance.has_as_course.extend(finance_courses)

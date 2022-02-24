"""Economy modules"""
from src.builder import ONTOLOGY
from src.construction.micro_learning.classes import Module
from src.instances.micro_learning.finance.courses import (
    business_finance,
    market_finance,
    insurance,
)
from src.instances.micro_learning.economy.modules import exchange_markets, interest_rate

with ONTOLOGY:
    # Market Finance course

    debt = Module("Debt")
    commodities = Module("Commodities")
    financial_value = Module("FinancialValue")

    lending = Module("Lending")
    federal_funds = Module("FederalFunds")
    market_capitalization = Module("MarketCapitalization")

    leverage = Module("Leverage")
    financial_regulation = Module("FinancialRegulation")
    capital_efficiency = Module("CapitalEfficiency")

    lending.requires_module.extend([debt, interest_rate])
    federal_funds.requires_module.extend([exchange_markets, lending])
    market_capitalization.requires_module.extend([debt, commodities, financial_value])
    leverage.requires_module.extend([lending])
    financial_regulation.requires_module.extend([exchange_markets, leverage])
    capital_efficiency.requires_modules.extend([lending])

    market_finance_modules = [
        debt,
        commodities,
        financial_value,
        lending,
        federal_funds,
        market_capitalization,
        leverage,
        financial_regulation,
        capital_efficiency,
    ]

    market_finance.has_as_module.extend(market_finance_modules)

    # Business Finance course

    stocks = Module("Stocks")
    bonds = Module("Bonds")

    intial_public_offering = Module("InitialPublicOffering")

    intial_public_offering.requires_module.extend([stocks, exchange_markets, financial_value])

    business_finance_modules = [
        stocks,
        bonds,
        intial_public_offering,
    ]

    business_finance.has_as_module.extend(business_finance_modules)

    # Insurance course

    risk_management = Module("RiskManagement")

    insurance_modules = [
        risk_management,
    ]

    insurance.has_as_module.extend(insurance_modules)

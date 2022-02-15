"""Economy modules"""
from src.construction.micro_learning.classes import Module
from src.instances.micro_learning.economy.courses import macroeconomy

# Macroeconomy course
national_accounts = Module("NationalAccounts")
gdp = Module("GDP")
price_index = Module("PriceIndex")

unemployement = Module("Unemployement")
inflation = Module("Inflation")
economic_cycles = Module("EconomicCycles")

money_market = Module("MoneyMarket")
supply_and_demand = Module("SupplyAndDemand")


consumption = Module("Consumption")
investment = Module("Investment")
governement_spending = Module("GovernementSpending")

central_bank = Module("CentralBank")
monetary_policy = Module("MonetaryPolicy")
budget_policy = Module("BudgetPolicy")

budget_policy.requires_modules.append(supply_and_demand)
monetary_policy.requires_modules.append(supply_and_demand)
central_bank.requires_modules.extend([governement_spending, investment, consumption])

exports_and_imports = Module("ExportsAndImports")
exchange_markets = Module("ExchangeMarket")
exports_and_imports.requires_modules.extend(
    [central_bank, monetary_policy, budget_policy]
)
exchange_markets.requires_modules.extend([central_bank, monetary_policy, budget_policy])

macroeconomy_modules = [
    unemployement,
    gdp,
    inflation,
    economic_cycles,
    money_market,
    supply_and_demand,
    central_bank,
    monetary_policy,
    budget_policy,
]

# Relations

macroeconomy.has_a_module.extend(macroeconomy_modules)

money_market.requires_modules.extend([unemployement, gdp, inflation, economic_cycles])

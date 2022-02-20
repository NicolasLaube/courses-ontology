"""Economy modules"""
from src.builder import ONTOLOGY
from src.construction.micro_learning.classes import Module
from src.instances.micro_learning.economy.courses import macroeconomy

with ONTOLOGY:
    # Macroeconomy course
    national_accounts = Module("NationalAccounts")
    gdp = Module("GDP")
    price_index = Module("PriceIndex")

    unemployement = Module("Unemployement")
    inflation = Module("Inflation")
    economic_cycles = Module("EconomicCycles")
    growth = Module("Growth")

    unemployement.requires_module.extend([national_accounts, gdp, price_index])
    inflation.requires_module.extend([national_accounts, gdp, price_index])
    economic_cycles.requires_module.extend([national_accounts, gdp, price_index])
    growth.requires_module.extend([national_accounts, gdp, price_index])

    money_market = Module("MoneyMarket")
    interest_rate = Module("InterestRate")
    credit_multiplier = Module("CreditMultiplier")

    money_market.requires_module.extend(
        [unemployement, inflation, economic_cycles, growth]
    )
    interest_rate.requires_module.extend(
        [unemployement, inflation, economic_cycles, growth]
    )
    credit_multiplier.requires_module.extend(
        [unemployement, inflation, economic_cycles, growth]
    )

    supply_and_demand = Module("SupplyAndDemand")
    consumption = Module("Consumption")
    investment = Module("Investment")
    governement_spending = Module("GovernementSpending")
    importations = Module("Importations")
    exportations = Module("Exportations")

    supply_and_demand.requires_module.extend(
        [money_market, interest_rate, credit_multiplier]
    )
    consumption.requires_module.extend([money_market, interest_rate, credit_multiplier])
    investment.requires_module.extend([money_market, interest_rate, credit_multiplier])
    governement_spending.requires_module.extend(
        [money_market, interest_rate, credit_multiplier]
    )
    importations.requires_module.extend(
        [money_market, interest_rate, credit_multiplier]
    )
    exportations.requires_module.extend(
        [money_market, interest_rate, credit_multiplier]
    )

    central_bank = Module("CentralBank")
    monetary_policy = Module("MonetaryPolicy")
    budget_policy = Module("BudgetPolicy")

    budget_policy.requires_module.extend(
        [
            supply_and_demand,
            consumption,
            investment,
            governement_spending,
            importations,
            exportations,
        ]
    )
    monetary_policy.requires_module.extend(
        [
            supply_and_demand,
            consumption,
            investment,
            governement_spending,
            importations,
            exportations,
        ]
    )
    central_bank.requires_module.extend(
        [
            supply_and_demand,
            consumption,
            investment,
            governement_spending,
            importations,
            exportations,
        ]
    )

    exchange_markets = Module("ExchangeMarket")
    exchange_markets.requires_module.extend(
        [central_bank, monetary_policy, budget_policy]
    )

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

    macroeconomy.has_as_module.extend(macroeconomy_modules)

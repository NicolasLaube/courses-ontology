"""Economy modules"""
from src.builder import ONTOLOGY
from src.construction.micro_learning.classes import Module
from src.instances.micro_learning.economy.courses import macroeconomy, micro_economics

with ONTOLOGY:
    # I- Introcution Micro economics

    # What is Economics
    wants_and_scarcity = Module("WantsAndScarcity")
    micro_and_macro_economics = Module("MicroAndMacroEconomics")
    positive_and_normative_economics = Module("PositiveAndNormativeEconomics")
    choices_and_tradeoffs = Module("ChoicesAndTradeOffs")
    economic_system_and_environnement = Module("TheEconomicSystemAndEnvironnement")

    positive_and_normative_economics.requires_module.append(micro_and_macro_economics)
    choices_and_tradeoffs.requires_module.append(positive_and_normative_economics)
    economic_system_and_environnement.requires_module.append(micro_and_macro_economics)

    # The economic problem
    opportunity_cost_and_production_possibility_curve = Module(
        "OpportunityCostAndProductionPossibilityCurve"
    )
    absolute_and_comparative_advatange = Module("AbsoluteAndComparativeAdvantage")
    gains_from_trade_and_eco_growth = Module("GainsFromTradeAndEconomicGrowth")
    free_vs_fair_trade = Module("FreeVSFairTrade")
    sustainability = Module("Sustainability")

    opportunity_cost_and_production_possibility_curve.requires_module.extend(
        [
            wants_and_scarcity,
            micro_and_macro_economics,
            positive_and_normative_economics,
            choices_and_tradeoffs,
            economic_system_and_environnement,
        ]
    )
    absolute_and_comparative_advatange.requires_module.extend(
        [
            wants_and_scarcity,
            micro_and_macro_economics,
            positive_and_normative_economics,
            choices_and_tradeoffs,
            economic_system_and_environnement,
        ]
    )
    gains_from_trade_and_eco_growth.requires_module.extend(
        [
            wants_and_scarcity,
            micro_and_macro_economics,
            positive_and_normative_economics,
            choices_and_tradeoffs,
            economic_system_and_environnement,
        ]
    )
    free_vs_fair_trade.requires_module.extend([gains_from_trade_and_eco_growth])
    sustainability.requires_module.extend([absolute_and_comparative_advatange])

    # Demand and supply
    law_of_demand = Module("LawOfDemand")
    law_of_supply = Module("LawOfSupply")
    equilibrium_price_and_quantity = Module("EquilibriumPriceAndQuantity")
    predicting_changes_in_price_and_quantity = Module(
        "PredictingChangesInPriceAndQuantity"
    )

    law_of_demand.requires_module.append(absolute_and_comparative_advatange)
    law_of_supply.requires_module.append(absolute_and_comparative_advatange)

    equilibrium_price_and_quantity.requires_module.extend(
        [law_of_demand, law_of_supply]
    )
    predicting_changes_in_price_and_quantity.requires_module.append(
        equilibrium_price_and_quantity
    )

    # Elasticity
    price_elasticity_demand = Module("PriceElasticityDemand")
    price_elasticity_supply = Module("PriceElasticitySupply")
    relationship_between_price_elast_demand_and_tot_revenue = Module(
        "RelationshipBetweenPriceElasticityOfDemandAndTotalRevenue"
    )
    income_elasticity_of_demand = Module("IncomeElastictyOfDemand")
    cross_elasticity_of_demand = Module("CrossElasticityOfDemand")
    influence_factors_of_elasticity = Module("InfluenceFactorsOfElasticity")

    price_elasticity_demand.requires_module.append(
        predicting_changes_in_price_and_quantity
    )
    price_elasticity_supply.requires_module.append(
        predicting_changes_in_price_and_quantity
    )
    relationship_between_price_elast_demand_and_tot_revenue.requires_module.extend(
        [price_elasticity_demand, price_elasticity_supply]
    )
    income_elasticity_of_demand.requires_module.extend(
        [price_elasticity_demand, price_elasticity_supply]
    )
    cross_elasticity_of_demand.requires_module.extend(
        [
            income_elasticity_of_demand,
            relationship_between_price_elast_demand_and_tot_revenue,
        ]
    )

    # Governement in action
    demand_and_margin_benefit = Module("DemandAndMarginBenefit")
    supply_and_marginal_cost = Module("SupplyAndMarginalCost")
    efficiency_of_competitive_market = Module("EfficiencyOfCompetitiveMarket")
    surpluses_and_shortages = Module("SurplusesAndShortages")
    minimum_wage_and_rent_control = Module("MinimumWageAndRentControl")
    taxes_and_subsidies = Module("TaxesAndSubsidies")

    demand_and_margin_benefit.requires_module.extend(
        [relationship_between_price_elast_demand_and_tot_revenue]
    )
    supply_and_marginal_cost.requires_module.extend(
        [
            relationship_between_price_elast_demand_and_tot_revenue,
            cross_elasticity_of_demand,
        ]
    )
    efficiency_of_competitive_market.requires_module.extend(
        [demand_and_margin_benefit, supply_and_marginal_cost]
    )
    surpluses_and_shortages.requires_module.extend(
        [demand_and_margin_benefit, efficiency_of_competitive_market]
    )
    minimum_wage_and_rent_control.requires_module.extend([cross_elasticity_of_demand])
    taxes_and_subsidies.requires_module.extend(
        [
            demand_and_margin_benefit,
            supply_and_marginal_cost,
            minimum_wage_and_rent_control,
        ]
    )

    # Utility and demand
    total_utility_and_marginal_utility = Module("TotalUtilityAndMarginalUtility")
    paradox_of_value = Module("ParadoxOfValue")
    overconsumption_and_social_norms = Module("OverconsumptionAndSocialNorms")

    total_utility_and_marginal_utility.requires_module.append(taxes_and_subsidies)
    paradox_of_value.requires_module.append(taxes_and_subsidies)
    overconsumption_and_social_norms.requires_module.extend(
        [taxes_and_subsidies, total_utility_and_marginal_utility]
    )

    # Possibilities, preferences and choices
    preferences_and_indefferences_curves = Module("PreferencesAndIndefferencesCurves")
    budget_schedule_and_budget_line = Module("BudgetScheduleAndBudgetLine")
    deriving_an_individual_demand_curve_and_pred_consum_choices = Module(
        "DerivingAnIndividualDemandCurveAndPredConsomChoices"
    )
    work_leisure_choices = Module("WorkLeisureChoices")

    preferences_and_indefferences_curves.requires_module.extend(
        [paradox_of_value, overconsumption_and_social_norms]
    )
    budget_schedule_and_budget_line.requires_module.append(
        preferences_and_indefferences_curves
    )
    deriving_an_individual_demand_curve_and_pred_consum_choices.requires_module.append(
        budget_schedule_and_budget_line
    )
    work_leisure_choices.requires_module.append(
        deriving_an_individual_demand_curve_and_pred_consum_choices
    )

    # Organizing production
    explicit_implicit_cost = Module("ExplicitImplicitCost")
    accounting_profits_vs_economic_efficiency = Module(
        "AccountingProfitsVSEconomicEfficiency"
    )
    technological_and_economic_efficiency = Module("TechnologicalAndEconomicEfficiency")
    markets_and_the_competitive_env = Module("MarketsAndTheComptetitiveEnvironnement")
    sustainable_business = Module("SustainableBusiness")
    triple_bottom_line = Module("TripleBottomLine")

    explicit_implicit_cost.requires_module.extend(
        [paradox_of_value, overconsumption_and_social_norms]
    )
    accounting_profits_vs_economic_efficiency.requires_module.append(
        explicit_implicit_cost
    )
    technological_and_economic_efficiency.requires_module.append(
        accounting_profits_vs_economic_efficiency
    )
    markets_and_the_competitive_env.requires_module.append(
        accounting_profits_vs_economic_efficiency
    )
    sustainable_business.requires_module.append(markets_and_the_competitive_env)
    triple_bottom_line.requires_module.append(markets_and_the_competitive_env)

    # Output and costs
    laws_of_production = Module("LawsOfProduction")
    product_curves = Module("ProductCurves")
    short_run_curves = Module("ShortRunCurves")
    long_run_curves = Module("LongRunCurves")

    laws_of_production.requires_module.append(markets_and_the_competitive_env)
    product_curves.requires_module.append(laws_of_production)
    short_run_curves.requires_module.append(product_curves)
    long_run_curves.requires_module.append(product_curves)

    # Perfect competition
    characteristics_of_perfect_competition = Module(
        "CharacteristicsOfPerfectCompettition"
    )
    profit_maximizing_condition_short_run = Module("ProfitMaximizingConditionShortRun")
    profit_maximizing_condition_long_run = Module("ProfitMaximizingContionLongRun")
    break_even_point = Module("BreakEvenPoint")
    shut_down_point = Module("ShutDownPoint")
    entry_and_exit = Module("EntryAndExit")

    characteristics_of_perfect_competition.requires_module.extend(
        [
            laws_of_production,
            product_curves,
            short_run_curves,
            long_run_curves,
        ]
    )
    profit_maximizing_condition_short_run.requires_module.append(
        characteristics_of_perfect_competition
    )
    profit_maximizing_condition_long_run.requires_module.append(
        characteristics_of_perfect_competition
    )
    break_even_point.requires_module.append(characteristics_of_perfect_competition)
    shut_down_point.requires_module.append(characteristics_of_perfect_competition)
    entry_and_exit.requires_module.append(characteristics_of_perfect_competition)

    # Monopoly
    characteristics_of_monopoly_market = Module("CharacteristicsOfMonopolyMarket")
    natural_monopoly = Module("NaturalMonopoly")
    price_discrimination = Module("PriceDiscrimination")
    comparing_price_out_between_monopoly_and_perfect_comp = Module(
        "ComparingPriceAndOutputBetweenMonopolyAndPerfectCompetition"
    )

    characteristics_of_monopoly_market.requires_module.extend(
        [
            profit_maximizing_condition_short_run,
            profit_maximizing_condition_long_run,
            break_even_point,
            shut_down_point,
            entry_and_exit,
        ]
    )
    natural_monopoly.requires_module.append(characteristics_of_monopoly_market)
    price_discrimination.requires_module.append(characteristics_of_monopoly_market)
    comparing_price_out_between_monopoly_and_perfect_comp.requires_module.extend(
        [natural_monopoly, price_discrimination]
    )
    # Monopolistic competition
    characteristics_of_monopolistic_competition = Module(
        "CharacteristicsOfMonopolisticCompetition"
    )
    price_and_output_in_monopolistic_competition = Module(
        "PriceAndOutputInMonopolisticCompetition"
    )

    characteristics_of_monopolistic_competition.requires_module.append(
        comparing_price_out_between_monopoly_and_perfect_comp
    )
    price_and_output_in_monopolistic_competition.requires_module.append(
        comparing_price_out_between_monopoly_and_perfect_comp
    )

    # Oligopoly
    what_is_oligopoly = Module("WhatIsOligopoly")
    kinked_demand_curve = Module("KinkedDemandCurve")
    dominant_firm_oligopoly = Module("DominantFirmOligopoly")
    oligopoly_games = Module("OligopolyGames")

    what_is_oligopoly.requires_module.extend(
        [
            price_and_output_in_monopolistic_competition,
            characteristics_of_monopolistic_competition,
        ]
    )

    kinked_demand_curve.requires_module.append(what_is_oligopoly)
    dominant_firm_oligopoly.requires_module.append(what_is_oligopoly)
    oligopoly_games.requires_module.append(what_is_oligopoly)

    micro_economics_modules = [
        oligopoly_games,
        dominant_firm_oligopoly,
        kinked_demand_curve,
        what_is_oligopoly,
        price_and_output_in_monopolistic_competition,
        characteristics_of_monopolistic_competition,
        comparing_price_out_between_monopoly_and_perfect_comp,
        price_discrimination,
        natural_monopoly,
        characteristics_of_monopoly_market,
        technological_and_economic_efficiency,
        markets_and_the_competitive_env,
        sustainable_business,
        triple_bottom_line,
        laws_of_production,
        product_curves,
        short_run_curves,
        long_run_curves,
        characteristics_of_perfect_competition,
        profit_maximizing_condition_short_run,
        profit_maximizing_condition_long_run,
        break_even_point,
        shut_down_point,
        entry_and_exit,
        wants_and_scarcity,
        micro_and_macro_economics,
        positive_and_normative_economics,
        choices_and_tradeoffs,
        economic_system_and_environnement,
        opportunity_cost_and_production_possibility_curve,
        absolute_and_comparative_advatange,
        gains_from_trade_and_eco_growth,
        free_vs_fair_trade,
        sustainability,
        law_of_demand,
        law_of_supply,
        equilibrium_price_and_quantity,
        predicting_changes_in_price_and_quantity,
        price_elasticity_demand,
        price_elasticity_supply,
        relationship_between_price_elast_demand_and_tot_revenue,
        income_elasticity_of_demand,
        cross_elasticity_of_demand,
        influence_factors_of_elasticity,
        demand_and_margin_benefit,
        supply_and_marginal_cost,
        efficiency_of_competitive_market,
        surpluses_and_shortages,
        minimum_wage_and_rent_control,
        taxes_and_subsidies,
        total_utility_and_marginal_utility,
        paradox_of_value,
        overconsumption_and_social_norms,
        preferences_and_indefferences_curves,
        budget_schedule_and_budget_line,
        deriving_an_individual_demand_curve_and_pred_consum_choices,
        work_leisure_choices,
        explicit_implicit_cost,
        accounting_profits_vs_economic_efficiency,
    ]

    micro_economics.has_as_module.extend(micro_economics_modules)

    # II- Macroeconomy course
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

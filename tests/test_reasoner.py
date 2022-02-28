"""Test the reasoner"""

from typing import Dict, List
import pytest

from src.reasoner import (
    get_module_level,
    get_all_dependencies,
    get_min_dependencies,
    get_all_modules_in_course,
    get_module_levels_in_course,
    get_min_dependencies_in_course,
)


@pytest.mark.graph_level
def test_module_level() -> None:
    """Tests the graph level of a module"""
    assert get_module_level("MicrobiotaPresentation", "Microbiota") == 0
    assert get_module_level("WomenInRockMusic", "RockMusic") == 30


@pytest.mark.all_dependencies
def test_module_all_dependencies() -> None:
    """Tests all dependencies getter for a module in a course"""
    assert get_all_dependencies("MicrobiotaPresentation", "Microbiota") == []
    assert set(get_all_dependencies("MicrobiotaMetaGenomicStudy", "Microbiota")) == set(
        [
            "ResearchesOnMicrobiota",
            "MicrobiotaAndDiabet",
            "MicrobiotaAndDigestion",
            "MicrobiotaAndDiabet",
            "MicrobiotaAndObesity",
            "MicrobiotaMetabolicFunction",
            "MicrobiotaAndPsychicState",
            "MicrobiotaAndAutism",
            "MicrobiotaAndBrainDevelopment",
            "MicrobiotaBrainIntestineAxis",
            "MicrobiotaRole",
            "MicrobiotaAndAntibiotics",
            "MicrobiotaDuringPregnancy",
            "MicrobiotaPathologies",
            "MicrobiotaThroughLife",
            "PhylogeneticKernel",
            "HumanMicrobiota",
            "MicrobiotaComposition",
            "EnvironmentInfluenceOnMicrobiota",
            "MicrobiotaSeasonalty",
            "MicrobiotaPresentation",
            "MicrobiotaStructure",
            "MicrobiotaPresentation",
        ]
    )


@pytest.mark.min_dependencies
def test_module_min_dependencies() -> None:
    """Tests the min dependencies of a module in a specific course"""
    assert get_min_dependencies("MicrobiotaPresentation", "Microbiota") == []
    assert get_min_dependencies("MicrobiotaMetaGenomicStudy", "Microbiota") == [
        "ResearchesOnMicrobiota"
    ]


@pytest.mark.all_dependencies
def test_all_modules_in_course() -> None:
    """Tests all the modules in a specific course"""
    assert get_all_modules_in_course("TheoryOfEvolution") == []
    assert set(get_all_modules_in_course("Microbiota")) == set(
        [
            "MicrobiotaAndDiabet",
            "MicrobiotaAndObesity",
            "MicrobiotaStructure",
            "MicrobiotaMetabolicFunction",
            "MicrobiotaAndChronicIntestineDiseases",
            "MicrobiotaStimulateImmuneSystem",
            "MicrobiotaAndImmuneSystem",
            "MicrobiotaRole",
            "MicrobiotaPathologies",
            "MicrobiotaAndAntibiotics",
            "MicrobiotaDuringPregnancy",
            "MicrobiotaThroughLife",
            "Enterotypes",
            "MicrobiotaMetaGenomicStudy",
            "PhylogeneticKernel",
            "MicrobiotaOnAxenicAnimals",
            "HumanMicrobiota",
            "MicrobiotaTaxonomy",
            "MicrobiotaComposition",
            "ResearchesOnMicrobiota",
            "FecalMicrobiotaTransplant",
            "MicrobiotaAndPsychicState",
            "EnvironmentInfluenceOnMicrobiota",
            "MicrobiotaAndAutism",
            "MicrobiotaAndBrainDevelopment",
            "MicrobiotaPresentation",
            "MicrobiotaBrainIntestineAxis",
            "MicrobiotaSeasonalty",
            "MicrobiotaAndDigestion",
        ]
    )


@pytest.mark.graph_level
def test_module_levels_in_course() -> None:
    """Tests the graph level of all the modules in a course"""
    assert get_module_levels_in_course("TheoryOfEvolution") == {}
    assert get_module_levels_in_course("Microbiota") == {
        "MicrobiotaPresentation": 0,
        "MicrobiotaStructure": 1,
        "MicrobiotaSeasonalty": 2,
        "EnvironmentInfluenceOnMicrobiota": 2,
        "FecalMicrobiotaTransplant": 3,
        "MicrobiotaComposition": 3,
        "HumanMicrobiota": 4,
        "PhylogeneticKernel": 5,
        "Enterotypes": 5,
        "MicrobiotaThroughLife": 6,
        "MicrobiotaDuringPregnancy": 7,
        "MicrobiotaAndAntibiotics": 7,
        "MicrobiotaPathologies": 7,
        "MicrobiotaRole": 8,
        "MicrobiotaAndImmuneSystem": 9,
        "MicrobiotaStimulateImmuneSystem": 10,
        "MicrobiotaAndChronicIntestineDiseases": 11,
        "MicrobiotaMetabolicFunction": 9,
        "MicrobiotaAndObesity": 10,
        "MicrobiotaAndDiabet": 11,
        "MicrobiotaAndDigestion": 12,
        "MicrobiotaBrainIntestineAxis": 9,
        "MicrobiotaAndBrainDevelopment": 10,
        "MicrobiotaAndAutism": 11,
        "MicrobiotaAndPsychicState": 12,
        "ResearchesOnMicrobiota": 13,
        "MicrobiotaTaxonomy": 14,
        "MicrobiotaOnAxenicAnimals": 14,
        "MicrobiotaMetaGenomicStudy": 14,
    }


@pytest.mark.min_dependencies
def test_course_min_dependencies() -> None:
    """Tests the min dependencies of all the module in a course"""
    assert get_min_dependencies_in_course("TheoryOfEvolution") == {}
    true_value: Dict[str, List[str]] = {
        "MicrobiotaAndDiabet": ["MicrobiotaAndObesity"],
        "MicrobiotaAndObesity": ["MicrobiotaMetabolicFunction"],
        "MicrobiotaStructure": ["MicrobiotaPresentation"],
        "MicrobiotaMetabolicFunction": ["MicrobiotaRole"],
        "MicrobiotaAndChronicIntestineDiseases": ["MicrobiotaStimulateImmuneSystem"],
        "MicrobiotaStimulateImmuneSystem": ["MicrobiotaAndImmuneSystem"],
        "MicrobiotaAndImmuneSystem": ["MicrobiotaRole"],
        "MicrobiotaRole": [
            "MicrobiotaAndAntibiotics",
            "MicrobiotaDuringPregnancy",
            "MicrobiotaPathologies",
        ],
        "MicrobiotaPathologies": ["MicrobiotaThroughLife"],
        "MicrobiotaAndAntibiotics": ["MicrobiotaThroughLife"],
        "MicrobiotaDuringPregnancy": ["MicrobiotaThroughLife"],
        "MicrobiotaThroughLife": ["PhylogeneticKernel"],
        "Enterotypes": ["HumanMicrobiota"],
        "MicrobiotaMetaGenomicStudy": ["ResearchesOnMicrobiota"],
        "PhylogeneticKernel": ["HumanMicrobiota"],
        "MicrobiotaOnAxenicAnimals": ["ResearchesOnMicrobiota"],
        "HumanMicrobiota": ["MicrobiotaComposition"],
        "MicrobiotaTaxonomy": ["ResearchesOnMicrobiota"],
        "MicrobiotaComposition": [
            "EnvironmentInfluenceOnMicrobiota",
            "MicrobiotaSeasonalty",
        ],
        "ResearchesOnMicrobiota": [
            "MicrobiotaAndDigestion",
            "MicrobiotaAndPsychicState",
        ],
        "FecalMicrobiotaTransplant": ["EnvironmentInfluenceOnMicrobiota"],
        "MicrobiotaAndPsychicState": ["MicrobiotaAndAutism"],
        "EnvironmentInfluenceOnMicrobiota": ["MicrobiotaStructure"],
        "MicrobiotaAndAutism": ["MicrobiotaAndBrainDevelopment"],
        "MicrobiotaAndBrainDevelopment": ["MicrobiotaBrainIntestineAxis"],
        "MicrobiotaPresentation": [],
        "MicrobiotaBrainIntestineAxis": ["MicrobiotaRole"],
        "MicrobiotaSeasonalty": ["MicrobiotaStructure"],
        "MicrobiotaAndDigestion": ["MicrobiotaAndDiabet"],
    }
    result_query = get_min_dependencies_in_course("Microbiota")
    assert len(true_value) == len(result_query)
    for key, list_modules in true_value.items():
        assert set(list_modules) == set(result_query[key])

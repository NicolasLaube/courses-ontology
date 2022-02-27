"""Test Person requests"""

import pytest

from src.builder import ONTOLOGY
from src.requests.requests_persons import (  # get_learner_accessible_courses,
    get_course_creators,
    get_course_finishers,
    get_unlocked_modules,
)

with ONTOLOGY:

    @pytest.mark.requests
    def test_course_creator() -> None:
        """Test course creators"""
        pop_creators = get_course_creators(ONTOLOGY.PopMusic)

        assert ONTOLOGY.Antoine in pop_creators

    @pytest.mark.requests
    def test_course_finishers() -> None:
        """Test course finishers"""
        print(get_course_finishers(ONTOLOGY.PopMusic))

        assert [ONTOLOGY.Beatrice, ONTOLOGY.Paola] == get_course_finishers(
            ONTOLOGY.PopMusic
        )

    @pytest.mark.requests
    def test_unlocked_modules() -> None:
        """Test unlocked modules"""
        unlocked_modules = [
            module_.name
            for module_ in get_unlocked_modules(
                ONTOLOGY.PopMusicFamousArtists, ONTOLOGY.Mathilde
            )
        ]
        assert ONTOLOGY.PopMusicFestivals.name in unlocked_modules

    # @pytest.mark.requests
    # def test_accessible_courses() -> None:
    #     """Test unlocked modules"""
    #     accesible_courses = sorted(
    #         [
    #             module_.name
    #             for module_ in get_learner_accessible_courses(ONTOLOGY.George)
    #         ]
    #     )
    #     true_accessible = sorted(
    #         [
    #             ONTOLOGY.Microbiota.name,
    #             ONTOLOGY.TheoryOfEvolution.name,
    #             ONTOLOGY.NumericEconomy.name,
    #             ONTOLOGY.CurrencyAndFinancialInstituations.name,
    #             ONTOLOGY.PovertyAndInequalities.name,
    #             ONTOLOGY.Macroeconomy.name,
    #             ONTOLOGY.PopMusic.name,
    #             ONTOLOGY.ClassicalMusic.name,
    #             ONTOLOGY.Microeconomics.name,
    #             ONTOLOGY.BusinessFinance.name,
    #             ONTOLOGY.MarketFinance.name,
    #             ONTOLOGY.Insurance.name,
    #         ]
    #     )

    #     assert true_accessible == accesible_courses

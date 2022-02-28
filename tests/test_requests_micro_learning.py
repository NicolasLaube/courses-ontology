"""Test Micro learning requests"""

import pytest

from src.builder import ONTOLOGY
from src.instances import pop_music_modules
from src.requests.requests_micro_learning import (
    get_all_courses,
    get_all_thematics,
    get_course_modules,
    get_course_prerequisites,
    get_course_thematics,
    get_module_prerequisites,
)

with ONTOLOGY:

    @pytest.mark.requests
    def test_courses_list() -> None:
        """Test course list"""
        true_courses_ = sorted(
            [
                ONTOLOGY.Microbiota.name,
                ONTOLOGY.TheoryOfEvolution.name,
                ONTOLOGY.NumericEconomy.name,
                ONTOLOGY.CurrencyAndFinancialInstituations.name,
                ONTOLOGY.PovertyAndInequalities.name,
                ONTOLOGY.Macroeconomy.name,
                ONTOLOGY.PopMusic.name,
                ONTOLOGY.ClassicalMusic.name,
                ONTOLOGY.RockMusic.name,
                ONTOLOGY.Microeconomics.name,
                ONTOLOGY.BusinessFinance.name,
                ONTOLOGY.MarketFinance.name,
                ONTOLOGY.Insurance.name,
            ]
        )
        assert true_courses_ == sorted([course_.name for course_ in get_all_courses()])

    @pytest.mark.requests
    def test_thematics_list() -> None:
        """Test thematics list"""
        true_thematics_ = sorted(
            [
                ONTOLOGY.Biology.name,
                ONTOLOGY.History.name,
                ONTOLOGY.Music.name,
                ONTOLOGY.Arts.name,
                ONTOLOGY.Literature.name,
                ONTOLOGY.Astronomy.name,
                ONTOLOGY.Geopolitics.name,
                ONTOLOGY.Economy.name,
                ONTOLOGY.InformationTechnologies.name,
                ONTOLOGY.Finance.name,
            ]
        )
        assert true_thematics_ == sorted(
            [thematic_.name for thematic_ in get_all_thematics()]
        )

    @pytest.mark.requests
    def test_course_modules() -> None:
        """Test course modules"""

        assert pop_music_modules == get_course_modules(ONTOLOGY.PopMusic)

    @pytest.mark.requests
    def test_course_thematic() -> None:
        """Test course thematic"""
        assert [ONTOLOGY.Music] == get_course_thematics(ONTOLOGY.PopMusic)

    @pytest.mark.requests
    def test_course_prerequisites() -> None:
        """Test course prerequisites"""
        assert [
            ONTOLOGY.PopMusicPresentation,
            ONTOLOGY.PopMusicOrigin,
            ONTOLOGY.PopMusic2000,
        ] == get_course_prerequisites(ONTOLOGY.RockMusic)

    @pytest.mark.requests
    def test_module_prerequisites() -> None:
        """Test module prerequisites"""
        assert [ONTOLOGY.PopMusicPresentation] == get_module_prerequisites(
            ONTOLOGY.PopMusicFamousArtists
        )

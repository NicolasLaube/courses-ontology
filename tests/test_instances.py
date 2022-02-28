"""Test instances"""

import pytest

from src.builder import ONTOLOGY

with ONTOLOGY:

    @pytest.mark.requests
    def test_learner_inference() -> None:
        """Test learner inference"""
        assert ONTOLOGY.Lea.is_a == [ONTOLOGY.Learner]

    @pytest.mark.requests
    def test_learner_inference_2() -> None:
        """Test learner inference"""
        assert ONTOLOGY.Beatrice.is_a == [ONTOLOGY.Learner]

    @pytest.mark.instances
    def test_person() -> None:
        """Test person"""

        assert ONTOLOGY.George.is_a == [ONTOLOGY.Person]

    @pytest.mark.instances
    def test_creator() -> None:
        """Test creator"""

        assert ONTOLOGY.Antoine.is_a == [ONTOLOGY.Creator]

    @pytest.mark.instances
    def test_learner() -> None:
        """Test learner"""

        assert ONTOLOGY.Beatrice.is_a == [ONTOLOGY.Learner]

    @pytest.mark.instances
    def test_follower() -> None:
        """Test follower"""

        assert ONTOLOGY.Lola.is_a == [ONTOLOGY.Follower, ONTOLOGY.Learner]

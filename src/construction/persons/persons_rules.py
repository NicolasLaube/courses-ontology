"""SWRL Rules"""
from owlready2 import Imp

from src.builder import ONTOLOGY

with ONTOLOGY:
    imp = Imp()

    # if a person finished a course he finished all modules
    imp.set_as_rule(
        """Personne(?p), Course(?c), finished(?p, ?c),
                         Module(?m) -> finished(?p, ?m)"""
    )

    # A person who started a module is a learner
    imp.set_as_rule(
        """Personne(?p), Module(?m), started(?p, ?m)
                          -> Learner(?p)"""
    )

    # A person who started a module is a learner
    imp.set_as_rule(
        """Personne(?p), Module(?m), started(?p, ?m)
                          -> Learner(?p)"""
    )

    # A person who created a module is a creator
    imp.set_as_rule(
        """Personne(?p), Module(?m), created(?p, ?m)
                          -> Creator(?p)"""
    )

    # A person who created a course is a creator
    imp.set_as_rule(
        """Personne(?p), Course(?c), created(?p, ?c)
                          -> Creator(?p)"""
    )

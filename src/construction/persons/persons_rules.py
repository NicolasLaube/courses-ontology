"""SWRL Rules"""
from owlready2 import Imp

from src.builder import ONTOLOGY

with ONTOLOGY:
    imp = Imp()

    # if a person finished a course he finished all modules
    imp.set_as_rule(
        """Person(?p), Course(?c), finished(?p, ?c),
                        has_as_module(?c, ?m), Module(?m) -> finished(?p, ?m)"""
    )

    # A person who started a module is a learner
    imp.set_as_rule(
        """Person(?p), Module(?m), started(?p, ?m)
                          -> Learner(?p)"""
    )

    # A person who started a course is a learner
    imp.set_as_rule(
        """Person(?p), Course(?m), started(?p, ?m)
                          -> Learner(?p)"""
    )

    # A person who created a module is a creator
    imp.set_as_rule(
        """Person(?p), Module(?m), created(?p, ?m)
                          -> Creator(?p)"""
    )

    # A person who created a course is a creator
    imp.set_as_rule(
        """Person(?p), Course(?c), created(?p, ?c)
                          -> Creator(?p)"""
    )

    # A person who follows another person is a Follower
    imp.set_as_rule(
        """Person(?p1), Person(?p2), follows(?p1, ?p2)
                          -> Follower(?p2)"""
    )

    # A person who reviews another person is a Reviewer
    imp.set_as_rule(
        """Person(?p1), Person(?p2), reviewed(?p1, ?p2)
                          -> Reviewer(?p2)"""
    )

"""SWRL Rules"""
from owlready2 import Imp

from src.builder import ONTOLOGY


def set_rules():
    """Set rules"""
    with ONTOLOGY:
        print("Rules setting")
        # FOLLOWER RULES
        # A person who follows another person is a Follower
        set_one_rule(
            """Person(?p1), Person(?p2), follows(?p1, ?p2)
                            -> Follower(?p1)"""
        )
        # CREATOR RULES
        # A person who created a course is a creator
        set_one_rule(
            """Person(?p), Course(?c), created_course(?p, ?c)
                            -> Creator(?p)"""
        )
        # A person who created a module is a creator
        set_one_rule(
            """Person(?p), Module(?c), created_module(?p, ?c)
                            -> Creator(?p)"""
        )
        # A person who finished a module also started it
        set_one_rule(
            """Person(?p), Module(?m), finished_module(?p, ?m)
                            -> started_module(?p, ?m)"""
        )
        # A person who finished a course also started it
        set_one_rule(
            """Person(?p), Course(?c), finished_course(?p, ?c)
                            -> started_course(?p, ?c)"""
        )

        # LEARNER RULES
        # A person who started a course is a Learner
        set_one_rule(
            """Person(?p), Course(?c), started_course(?p, ?c)
                            -> Learner(?p)"""
        )
        # A person who started a module is a Learner
        set_one_rule(
            """Person(?p), Module(?m), started_module(?p, ?m)
                            -> Learner(?p)"""
        )
        # A person who started a course is a Learner
        set_one_rule(
            """Person(?p), Course(?c), finished_course(?p, ?c)
                            -> Learner(?p)"""
        )
        # A person who finsished a module is a Learner
        set_one_rule(
            """Person(?p), Module(?m), finished_module(?p, ?m)
                            -> Learner(?p)"""
        )

        # Finishers
        # if a person finished a course he finished all modules
        set_one_rule(
            """Person(?p), Course(?c), finished_course(?p, ?c), Module(?m),
                            has_as_module(?c, ?m) -> finished_module(?p, ?m)"""
        )

        # Reviewer
        # A person who reviews another person is a Reviewer
        set_one_rule(
            """Person(?p1), Person(?p2), reviewed(?p1, ?p2)
                            -> Reviewer(?p1)"""
        )


def set_one_rule(rule: str):
    """Sets one rule"""
    with ONTOLOGY:
        imp = Imp()
        imp.set_as_rule(rule)

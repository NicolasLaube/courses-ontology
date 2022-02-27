"""SWRL Rules"""
from owlready2 import Imp

from src.builder import ONTOLOGY

with ONTOLOGY:
    imp = Imp()

    # FOLLOWER RULES
    # A person who follows another person is a Follower
    imp.set_as_rule(
        """Person(?p1), Person(?p2), follows(?p1, ?p2)
                          -> Follower(?p1)"""
    )
    # CREATOR RULES
    # A person who created a course is a creator
    imp.set_as_rule(
        """Person(?p), Course(?c), created_course(?p, ?c)
                          -> Creator(?p)"""
    )
    # A person who created a module is a creator
    imp.set_as_rule(
        """Person(?p), Module(?c), created_module(?p, ?c)
                          -> Creator(?p)"""
    )

    # A person who finished a module also started it
    imp.set_as_rule(
        """Person(?p), Module(?m), finished_module(?p, ?m)
                          -> started_module(?p, ?m)"""
    )
    # A person who finished a course also started it
    imp.set_as_rule(
        """Person(?p), Course(?c), finished_course(?p, ?c)
                          -> started_course(?p, ?c)"""
    )

    # LEARNER RULES
    # A person who started a course is a Learner
    imp.set_as_rule(
        """Person(?p), Course(?c), started_course(?p, ?c)
                          -> Learner(?p)"""
    )
    # A person who started a module is a Learner
    imp.set_as_rule(
        """Person(?p), Module(?m), started_module(?p, ?m)
                          -> Learner(?p)"""
    )
    # A person who started a course is a Learner
    imp.set_as_rule(
        """Person(?p), Course(?c), finished_course(?p, ?c)
                          -> Learner(?p)"""
    )
    # A person who finsished a module is a Learner
    imp.set_as_rule(
        """Person(?p), Module(?m), finished_module(?p, ?m)
                          -> Learner(?p)"""
    )

    # Finishers
    # A person who finsished all module of course, finsihed the course
    imp.set_as_rule(
        """Person(?p), Course(?c), Module(?m), finished_module(?p, ?m), has_as_module(?c, ?m)
                          -> finished_course(?c)"""
    )

    # #if a person finished a course he finished all modules
    # imp.set_as_rule(
    #     """Person(?p), Course(?c), finished_course(?p, ?c),
    #                     has_as_module(?c, ?m), Module(?m) -> finished_module(?p, ?m)"""
    # )

    # # if a person finished a module he started it
    # imp.set_as_rule(
    #     """Person(?p), Module(?m), finished_module(?p, ?m),
    #                     -> started_module(?p, ?m)"""
    # )

    # # if a person finished all modules he finished the course
    # # imp.set_as_rule(
    # #     """Person(?p), Module(?m), Course(?c), has_as_module(?c, ?m), finished_module(?p, ?m),
    # #                     -> finished_course(?p, ?c)"""
    # # )

    # # if a person started a module he started the course
    # imp.set_as_rule(
    #     """Person(?p), Module(?m), started_module(?p, ?m), Course(?c),
    #                     has_as_module(?c, ?m) -> started_course(?p, ?c)"""
    # )

    # # A person who started a module is a learner
    # imp.set_as_rule(
    #     """Person(?p), Module(?m), started_module(?p, ?m)
    #                       -> Learner(?p)"""
    # )
    # # A person who started a module is a learner
    # imp.set_as_rule(
    #     """Person(?p), Module(?m), finished_module(?p, ?m)
    #                       -> Learner(?p)"""
    # )

    # # A person who started a course is a learner
    # imp.set_as_rule(
    #     """Person(?p), Course(?m), started_course(?p, ?m)
    #                       -> Learner(?p)"""
    # )

    # A person who created a module is a creator
    # imp.set_as_rule(
    #     """Person(?p), Module(?m), created_module(?p, ?m)
    #                       -> Creator(?p)"""
    # )

    # A person who reviews another person is a Reviewer
    # imp.set_as_rule(
    #     """Person(?p1), Person(?p2), reviewed(?p1, ?p2)
    #                       -> Reviewer(?p2)"""
    # )

    # A person who finished a course didn't fail it
    # imp.set_as_rule(
    #     """Person(?p), Course(?c), finished(?p, ?c)
    #                       -> not(failed(?p, ?c))"""
    # )

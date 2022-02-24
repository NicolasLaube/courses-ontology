"""Requests on persons"""
# pylint: disable=C0209, E0401
from typing import List

from owlready2 import default_world

from src.builder import ONTOLOGY
from src.construction import Course, Learner, Module

with ONTOLOGY:

    GRAPH = default_world.as_rdflib_graph()
    # @prefix ns1: <file://C:/Users/nicol/Documents/CS/3A/CR/projet/cr/storage/capsule.owl#> .
    # @prefix owl: <http://www.w3.org/2002/07/owl#> .
    # @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    # @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    # @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

    def get_unlocked_modules(module: Module, learner: Learner):
        """What modules are unlocked by user Y when finishing module X?"""
        return list(
            GRAPH.query_owlready(
                """SELECT ?b WHERE {
                    ?b a ns2:Module .
                    ?b ns2:requires_module <%s> .

                    OPTIONAL {
                        ?b ns2:requires_module ?m1 .
                        <%s> ns1:finished ?m1 .
                        FILTER (?m1 != <%s>) .
                    }
                    OPTIONAL {
                        <%s> ns1:finished ?m2 .
                        FILTER (?m1 = ?m2) .
                    }
                    FILTER(!bound(?m1)) .
                    FILTER(!bound(?m2)) .
                }
                """
                % (
                    module.iri,
                    learner.iri,
                    module.iri,
                    learner.iri,
                )
            )
        )

    def get_course_finishers(course: Course) -> List[str]:
        """Who finished Course X?"""
        return list(
            GRAPH.query_owlready(
                """SELECT ?b WHERE {
                    ?b a ns1:Person .
                    ?b ns1:finished <%s> .
                }"""
                % course.iri
            )
        )

    def get_course_creators(course: Course) -> List[str]:
        """Who created Course X?"""
        return list(
            GRAPH.query_owlready(
                """SELECT ?b WHERE {
                    ?b a ns1:Person .
                    ?b ns1:created <%s> .
                }"""
                % course.iri
            )
        )

    def get_learner_knowledge(learner: Learner) -> List[str]:
        """What is the knowledge of learner X?"""
        return list(
            GRAPH.query_owlready(
                """SELECT ?b WHERE {
                    ?b a ns1:Knowledge .
                    ?b ns1:is_in_module ?m .
                    <%s> ns1:finished ?m .
                }
                """
                % learner.iri
            )
        )

    # def get_learner_accessible_courses(learner: Learner):
    #     """Get all modules of the course"""
    #     # return list(
    #     #     GRAPH.query_owlready(
    #     #         """SELECT ?b WHERE {
    #     #             ?b a ns1:Module .
    #     #             <%s> ns1:has_as_module ?b .
    #     #         }
    #     #         """
    #     #         % course.iri
    #     #     )
    #     # )

    def get_modules_to_revise(learner: Learner):
        """What are the Modules that Learner Y should revise?"""
        return list(
            GRAPH.query_owlready(
                """SELECT ?b WHERE {
                    ?b a ns1:Module .
                    <%s> ns1:started ?b .
                    FILTER NOT EXIST {<%s> ns1:finished ?b}
                }
                """
                % (learner.iri, learner.iri)
            )
        )

    # def get_learner_position(learner: Learner, course: Course):
    #     """Where is the learner X in Course Y?"""

    # def get_accessible_modules(learner: Learner):
    #     """What Modules are accessible to learner?"""
    #     return list(
    #         GRAPH.query_owlready(
    #             """SELECT ?b WHERE {
    #                 ?b a ns1:Module .
    #                 FILTER NOT EXIST {
    #                     ?b requires_module ?m .
    #                     ! (?m ns1:was_finished_by <%s>) .
    #                 }
    #             } LIMIT 50
    #             """
    #         )
    #     )

    def get_number_starters(course: Course):
        """How many persons started the course X?"""
        return list(
            GRAPH.query_owlready(
                """SELECT COUNT(?b) WHERE {
                    ?b a ns1:Person .
                    ?b ns1:started ?m .
                    <%s> ns1:has_as_module ?m .
                }
                """
                % course.iri,
            )
        )

    def get_number_finishers(course: Course):
        """How many persons finished the course X?"""
        return list(
            GRAPH.query_owlready(
                """SELECT COUNT(?p) WHERE {
                    ?p a ns1:Person .
                    ?p ns1:finished <%s> .
                }
                """
                % course.iri
            )
        )

    # def get_seen_fragments(learner: Learner):
    #     """Get modules unlocked when a module is finished"""

    # print("### Get all thematics ###")
    # print(get_all_thematics())
    # print("### Get all courses ###")
    # pprint(get_all_courses())
    # print("### Thematics of course ###")
    # pprint(thematics_of_course(ONTOLOGY.PopMusic))
    # print("### Modules of course ###")
    # pprint(get_course_modules(ONTOLOGY.PopMusic))
    # print("### Knowledge of course ###")
    # pprint(get_course_knowledge(ONTOLOGY.PopMusic))
"""Requests on persons"""
# pylint: disable=C0209
# from pprint import pprint
# from typing import List

from owlready2 import default_world

from src.builder import ONTOLOGY

# from src.construction import Course, Learner

with ONTOLOGY:

    GRAPH = default_world.as_rdflib_graph()
    # @prefix ns1: <file://C:/Users/nicol/Documents/CS/3A/CR/projet/cr/storage/capsule.owl#> .
    # @prefix owl: <http://www.w3.org/2002/07/owl#> .
    # @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    # @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    # @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

    # def get_course_finishers(course: Course) -> List[str]:
    #     """Who finished Course X?"""

    # def get_course_creator(course: Course) -> List[str]:
    #     """Who created Course X?"""
    #     # return list(GRAPH.query_owlready("SELECT ?b WHERE { ?b a ns1:Course . }"))

    # def get_learner_knowledge(learner: Learner) -> List[str]:
    #     """What is the knowledge of learner X?"""
    #     # return list(
    #     #     GRAPH.query_owlready(
    #     #         """SELECT ?b WHERE {
    #     #             ?b a ns1:Thematic .
    #     #             <%s> ns1:is_in_thematic ?b .
    #     #         }
    #     #         """
    #     #         % learner.iri
    #     #     )
    #     # )

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

    # def get_courses_to_revise(learner: Learner):
    #     """What are the Courses that Learner Y should revise?"""
    #     # return list(
    #     #     GRAPH.query_owlready(
    #     #         """SELECT ?b WHERE {
    #     #             ?b a ns1:Knowledge .
    #     #             ?m ns1:contains_knowledge ?b .
    #     #             <%s> ns1:has_as_module ?b .
    #     #         }
    #     #         """
    #     #         % course.iri
    #     #     )
    #     # )

    # def get_learner_position(learner: Learner, course: Course):
    #     """Where is the learner X in Course Y?"""

    # def get_unlocked_modules(learner: Learner, course: Course):
    #     """What Modules were ?"""

    # def get_number_starters(course: Course):
    #     """How many persons started the course X?"""

    # def get_number_finishers(course: Course):
    #     """How many persons finished the course X?"""

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

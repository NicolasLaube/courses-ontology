"""SPARQL requests on courses"""
# pylint: disable=C0209, E0401
from typing import List

from owlready2 import default_world

from src.builder import ONTOLOGY
from src.construction import Course, Knowledge, Module, Thematic

with ONTOLOGY:

    GRAPH = default_world.as_rdflib_graph()
    # @prefix ns1: <file://C:/Users/nicol/Documents/CS/3A/CR/projet/cr/storage/capsule.owl#> .
    # @prefix owl: <http://www.w3.org/2002/07/owl#> .
    # @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    # @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    # @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
    GRAPH.serialize(destination="output.txt", format="turtle")

    def get_all_thematics() -> List[Thematic]:
        """What are all thematics?"""
        return [
            ele[0]
            for ele in list(
                GRAPH.query_owlready("SELECT ?b WHERE { ?b a ns1:Thematic . }")
            )
        ]

    def get_all_courses() -> List[Course]:
        """What are all available courses?"""
        return [
            ele[0]
            for ele in list(
                GRAPH.query_owlready("SELECT ?b WHERE { ?b a ns1:Course . }")
            )
        ]

    def get_course_thematics(course: Course) -> List[Course]:
        """To which thematic(s) is course X associated?"""
        return [
            ele[0]
            for ele in list(
                GRAPH.query_owlready(
                    """SELECT ?b WHERE {
                    ?b a ns1:Thematic .
                    <%s> ns1:is_in_thematic ?b .
                }
                """
                    % course.iri
                )
            )
        ]

    def get_course_modules(course: Course) -> List[Module]:
        """What are the modules of course X?"""
        return [
            ele[0]
            for ele in list(
                GRAPH.query_owlready(
                    """SELECT ?b WHERE {
                    ?b a ns1:Module .
                    <%s> ns1:has_as_module ?b .
                }
                """
                    % course.iri
                )
            )
        ]

    def get_module_knowledge(module: Module) -> List[Knowledge]:
        """What knwoledge is acquired thanks to module X?"""
        return [
            ele[0]
            for ele in list(
                GRAPH.query_owlready(
                    """SELECT ?b WHERE {
                    ?b a ns1:Knowledge .
                    <%s> ns1:contains_knowledge ?b .
                }
                """
                    % module.iri
                )
            )
        ]

    def get_course_knowledge(course: Course) -> List[Knowledge]:
        """What knowledge is acquired thanks to course X?"""
        return [
            ele[0]
            for ele in list(
                GRAPH.query_owlready(
                    """SELECT ?b WHERE {
                    ?b a ns1:Knowledge .
                    ?m ns1:contains_knowledge ?b .
                    <%s> ns1:has_as_module ?b .
                }
                """
                    % course.iri
                )
            )
        ]

    def get_module_prerequisites(module: Module) -> List[Module]:
        """What are the modules required for module X?"""
        return [
            ele[0]
            for ele in list(
                GRAPH.query_owlready(
                    """SELECT DISTINCT ?b WHERE {
                    ?b a ns1:Module .
                    <%s> ns1:requires_module ?b .
                }
                """
                    % module.iri
                )
            )
        ]

    def get_course_prerequisites(course: Course) -> List[Module]:
        """What are the modules required for course X?"""
        return [
            ele[0]
            for ele in list(
                GRAPH.query_owlready(
                    """SELECT DISTINCT ?b WHERE {
                    ?b a ns1:Module .
                    <%s> ns1:has_as_module ?d .
                    ?d ns1:requires_module ?b .
                    MINUS {
                        <%s> ns1:has_as_module ?b .
                    }
                }
                """
                    % (course.iri, course.iri)
                )
            )
        ]

    # def get_course_duration(course_name: str):
    #     """Get the duration of a course"""

    # def get_knowledge_duration(knowledge_name: str):
    #     """Get duration of knowledge acquisition"""

    # def get_module_duration(module_name: str):
    #     """Get module duration"""

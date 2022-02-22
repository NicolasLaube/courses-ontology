"""SPARQL requests on courses"""
# pylint: disable=C0209, E0401
from typing import List

from owlready2 import default_world

from src.builder import ONTOLOGY
from src.construction import Course, Module

with ONTOLOGY:

    GRAPH = default_world.as_rdflib_graph()
    # @prefix ns1: <file://C:/Users/nicol/Documents/CS/3A/CR/projet/cr/storage/capsule.owl#> .
    # @prefix owl: <http://www.w3.org/2002/07/owl#> .
    # @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    # @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    # @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
    GRAPH.serialize(destination="output.txt", format="turtle")

    def get_all_thematics() -> List[str]:
        """What are all thematics?"""
        return list(GRAPH.query_owlready("SELECT ?b WHERE { ?b a ns2:Thematic . }"))

    def get_all_courses() -> List[str]:
        """What are all available courses?"""
        return list(GRAPH.query_owlready("SELECT ?b WHERE { ?b a ns2:Course . }"))

    def get_course_thematics(course: Course) -> List[str]:
        """To which thmatic(s) is course X assoicated?"""
        return list(
            GRAPH.query_owlready(
                """SELECT ?b WHERE {
                    ?b a ns2:Thematic .
                    <%s> ns2:is_in_thematic ?b .
                }
                """
                % course.iri
            )
        )

    def get_course_modules(course: Course):
        """What are the modules of course X?"""
        return list(
            GRAPH.query_owlready(
                """SELECT ?b WHERE {
                    ?b a ns2:Module .
                    <%s> ns2:has_as_module ?b .
                }
                """
                % course.iri
            )
        )

    def get_module_knowledge(module: Module):
        """What knwoledge is acquired thanks to module X?"""
        return list(
            GRAPH.query_owlready(
                """SELECT ?b WHERE {
                    ?b a ns2:Knowledge .
                    <%s> ns2:contains_knowledge ?b .
                }
                """
                % module.iri
            )
        )

    def get_course_knowledge(course: Course):
        """What knowledge is acquired thanks to course X?"""
        return list(
            GRAPH.query_owlready(
                """SELECT ?b WHERE {
                    ?b a ns2:Knowledge .
                    ?m ns2:contains_knowledge ?b .
                    <%s> ns2:has_as_module ?b .
                }
                """
                % course.iri
            )
        )

    def get_prerequisites(module: Module):
        """What are the modules required for module X?"""
        return list(
            GRAPH.query_owlready(
                """SELECT ?b WHERE {
                    ?b a ns2:Module .
                    <%s> ns2:requires_module ?b .
                }
                """
                % module.iri
            )
        )

    # def get_course_duration(course_name: str):
    #     """Get the duration of a course"""

    # def get_knowledge_duration(knowledge_name: str):
    #     """Get duration of knowledge acquisition"""

    # def get_module_duration(module_name: str):
    #     """Get module duration"""

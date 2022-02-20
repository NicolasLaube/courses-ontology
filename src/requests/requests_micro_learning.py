"""All SPARQL requests on OWL"""
# pylint: disable=C0209
from pprint import pprint
from typing import List

from owlready2 import default_world

from src.builder import ONTOLOGY
from src.construction import Course

with ONTOLOGY:

    GRAPH = default_world.as_rdflib_graph()
    # @prefix ns1: <file://C:/Users/nicol/Documents/CS/3A/CR/projet/cr/storage/capsule.owl#> .
    # @prefix owl: <http://www.w3.org/2002/07/owl#> .
    # @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    # @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    # @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
    GRAPH.serialize(destination="output.txt", format="turtle")

    def get_all_thematics() -> List[str]:
        """Get all thematics"""
        return list(GRAPH.query_owlready("SELECT ?b WHERE { ?b a ns1:Thematic . }"))

    def get_all_courses() -> List[str]:
        """Get all thematics"""
        return list(GRAPH.query_owlready("SELECT ?b WHERE { ?b a ns1:Course . }"))

    def thematics_of_course(course: Course) -> List[str]:
        """Get Thematic(s) of course"""
        return list(
            GRAPH.query_owlready(
                """SELECT ?b WHERE {
                    ?b a ns1:Thematic .
                    <%s> ns1:is_in_thematic ?b .
                }
                """
                % course.iri
            )
        )

    def get_course_modules(course: Course):
        """Get all modules of the course"""
        return list(
            GRAPH.query_owlready(
                """SELECT ?b WHERE {
                    ?b a ns1:Module .
                    <%s> ns1:has_as_module ?b .
                }
                """
                % course.iri
            )
        )

    def get_course_knowledge(course: Course):
        """Get all knowledge acquired thanks to a course"""
        return list(
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

    # def get_next_module(module_name: str):
    #     """Get the module(s) immediately following module X"""

    # def get_unlocked_modules(module_name: str):
    #     """Get modules unlocked when a module is finished"""

    # def get_course_duration(course_name: str):
    #     """Get the duration of a course"""

    # def get_knowledge_duration(knowledge_name: str):
    #     """Get duration of knowledge acquisition"""

    # def get_module_duration(module_name: str):
    #     """Get module duration"""

    print("### Get all thematics ###")
    print(get_all_thematics())
    print("### Get all courses ###")
    pprint(get_all_courses())
    print("### Thematics of course ###")
    pprint(thematics_of_course(ONTOLOGY.PopMusic))
    print("### Modules of course ###")
    pprint(get_course_modules(ONTOLOGY.PopMusic))
    print("### Knowledge of course ###")
    pprint(get_course_knowledge(ONTOLOGY.PopMusic))

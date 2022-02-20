"""All SPARQL requests on OWL"""
from typing import List

from owlready2 import default_world

from src.builder import ONTOLOGY

with ONTOLOGY:

    GRAPH = default_world.as_rdflib_graph()
    # GRAPH.parse(ONTOLOGY_IRI, format="nt")
    GRAPH.bind("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    GRAPH.bind("rdfs", "http://www.w3.org/2000/01/rdf-schema#")
    # GRAPH.bind("base", ONTOLOGY_IRI)

    # In sparql requests,
    # w3C:type is equivalent to <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>

    def get_all_thematics() -> List[str]:
        """Get all thematics"""
        return list(GRAPH.query_owlready("SELECT ?b WHERE { ?b a rdfs:Class . }"))

    # def thematics_of_course(course_name: str) -> List[str]:
    #     """Get Thematic(s) of course"""

    # def get_course_modules(course_name: str):
    #     """Get all modules of the course"""

    # def get_course_knowledge(course_name: str):
    #     """Get all knowledge acquired thanks to a course"""

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

    print(get_all_thematics())

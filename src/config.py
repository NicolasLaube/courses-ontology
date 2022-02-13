"""Config"""
import owlready2 as owl

ONTOLOGY_IRI = "http://test.org/onto.owl"


ONTOLOGY = owl.get_ontology(ONTOLOGY_IRI)

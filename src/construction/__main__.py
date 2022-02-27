"""Main file"""
from owlready2 import OwlReadyInconsistentOntologyError, sync_reasoner_pellet

from src.builder import ONTOLOGY, ONTOLOGY_PATH, save_ontology

with ONTOLOGY:
    try:
        sync_reasoner_pellet(
            infer_property_values=True, infer_data_property_values=True
        )
    except OwlReadyInconsistentOntologyError as e:
        print("Error: ", str(e))
        print("Ontology is inconsistent")

print(ONTOLOGY, ONTOLOGY_PATH)
save_ontology(ONTOLOGY, ONTOLOGY_PATH)

print(ONTOLOGY.Abba.is_a)

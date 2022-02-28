"""Main file"""
from owlready2 import OwlReadyInconsistentOntologyError, sync_reasoner_pellet

from src.builder import ONTOLOGY, ONTOLOGY_PATH, save_ontology
from src.construction.persons.persons_rules import set_rules

with ONTOLOGY:

    try:
        set_rules()

        sync_reasoner_pellet(
            infer_property_values=True, infer_data_property_values=True
        )

        print(list(ONTOLOGY.rules()))
    except OwlReadyInconsistentOntologyError as e:
        print("Error: ", str(e))
        print("Ontology is inconsistent")

save_ontology(ONTOLOGY, ONTOLOGY_PATH)

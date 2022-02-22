"""Use of Pellet or Hermit reasoners"""
from owlready2 import OwlReadyInconsistentOntologyError, sync_reasoner_pellet

from src.builder import ONTOLOGY

with ONTOLOGY:
    try:
        sync_reasoner_pellet(
            infer_property_values=True, infer_data_property_values=True
        )
    except OwlReadyInconsistentOntologyError:
        print("Ontology is inconsistent")

"""Config"""
import os

from owlready2 import get_ontology

# It is better to import owlready2 with from owlready2 import * because
# Owlready redefines some python functions such as issubclass()

ONTOLOGY_IRI = "http://www.kapsule.com/kapsule.owl"


ONTOLOGY = get_ontology(ONTOLOGY_IRI)
ONTOLOGY_LOCAL_SAVE_PATH = os.path.join("data", "kaspule.owl")

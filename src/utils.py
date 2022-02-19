"""Utils functions"""
import os
from pprint import pprint

from owlready2 import get_ontology

from src import config


def load_ontology(
    ontology_path: str = config.ONTOLOGY_LOCAL_SAVE_PATH, is_local: bool = True
):
    """Loads an ontology from local path or web url"""
    if is_local:
        return get_ontology(os.path.abspath(ontology_path)).load(reload=True)
    return get_ontology(ontology_path).load(
        reload=True
    )  # forces reloading of ontology (cache deletion)


def show_informations(ontology):
    """Shows a few information on the ontology"""
    print(f"Base IRI: {ontology.base_iri}")
    print(f"Imported onotologies: {ontology.imported_ontologies}")
    print("Onotology classes: ")
    pprint(list(ontology.classes()))

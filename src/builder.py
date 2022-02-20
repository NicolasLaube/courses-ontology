"""Config"""
import os
from pprint import pprint

from owlready2 import default_world, get_ontology, onto_path  # type: ignore

# It is better to import owlready2 with from owlready2 import * because
# Owlready redefines some python functions such as issubclass()
ONTOLOGY_PATH = os.path.join("storage", "capsule.owl")
ONTOLOGY_IRI = ("file://" + ONTOLOGY_PATH).replace("\\", "/")
SQLITE3_PATH = os.path.abspath(os.path.join("storage", "capsule.sqlite3"))


def load_ontology():
    """Loads an ontology from local path or web url"""
    onto_path.append(ONTOLOGY_PATH)
    onto = get_ontology(ONTOLOGY_IRI)
    onto.load()
    return onto
    # forces reloading of ontology (cache deletion)


def save_ontology(onto, save_path: str = ONTOLOGY_PATH):
    """Saves an ontology"""
    onto.save(save_path, format="rdfxml")
    default_world.save()


def show_informations(ontology):
    """Shows a few information on the ontology"""
    print(f"Base IRI: {ontology.base_iri}")
    print(f"Imported ontologies: {ontology.imported_ontologies}")
    print("Onotology classes: ")
    pprint(list(ontology.classes()))


default_world.set_backend(filename=SQLITE3_PATH)
if os.path.exists(ONTOLOGY_PATH):
    print("Ok")
    ONTOLOGY = load_ontology()
else:
    ONTOLOGY = get_ontology(ONTOLOGY_IRI)

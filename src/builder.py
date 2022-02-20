"""Config"""
import os
from datetime import datetime
from pprint import pprint

from owlready2 import (  # type: ignore
    declare_datatype,
    default_world,
    get_ontology,
    onto_path,
)

# It is better to import owlready2 with from owlready2 import * because
# Owlready redefines some python functions such as issubclass()
ONTOLOGY_URL = "http://capsule.com/ontology.owl"
ONTOLOGY_PATH = os.path.abspath(os.path.join("storage", "capsule.owl"))
ONTOLOGY_IRI = ("file://" + ONTOLOGY_PATH).replace("\\", "/")
SQLITE3_PATH = os.path.abspath(os.path.join("storage", "capsule.sqlite3"))


def load_ontology():
    """Loads an ontology from local path or web url"""
    onto_path.append(ONTOLOGY_PATH)
    onto = get_ontology(ONTOLOGY_URL)
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
    print(f"Imported onotologies: {ontology.imported_ontologies}")
    print("Onotology classes: ")
    pprint(list(ontology.classes()))


class Time:
    """
    Time class
    ---
    Added because of error:
    Exception in thread "main" org.semanticweb.HermiT.
    datatypes.UnsupportedDatatypeException: HermiT supports
     all and only the datatypes of the OWL 2 datatype map, see
    http://www.w3.org/TR/owl2-syntax/#Datatype_Maps.
    The datatype 'http://www.w3.org/2001/XMLSchema#time' is not
    part of the OWL 2 datatype map and
    no custom datatype definition is given;
    therefore, HermiT cannot handle this datatype.
    """

    def __init__(self, value) -> None:
        self.value = value


def time_parser(time_as_string: str):
    """Time parser"""
    return Time(datetime.strptime(time_as_string, "%d/%m/%y %H:%M:%S"))


def time_unparser(time_obj: Time) -> str:
    """Time unparser"""
    return datetime.strftime(time_obj.value, "%d/%m/%y %H:%M:%S")


# The datatype must be declared BEFORE loading any ontology that uses it.
declare_datatype(
    Time, "https://www.w3.org/2001/XMLSchema#time", time_parser, time_unparser
)

default_world.set_backend(filename=SQLITE3_PATH)
if os.path.exists(ONTOLOGY_IRI):
    ONTOLOGY = load_ontology()
else:
    ONTOLOGY = get_ontology(ONTOLOGY_IRI)

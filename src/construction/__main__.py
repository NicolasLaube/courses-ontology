"""Main file"""
from src.builder import ONTOLOGY, ONTOLOGY_PATH, save_ontology

# ONTOLOGY.save(file=ONTOLOGY_IRI, format="ntriples")

save_ontology(ONTOLOGY, ONTOLOGY_PATH)
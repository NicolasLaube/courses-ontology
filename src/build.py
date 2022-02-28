"""Main file"""
from src.builder import ONTOLOGY, ONTOLOGY_PATH, save_ontology
from src.reasoner import save_levels_dependencies

# ONTOLOGY.save(file=ONTOLOGY_IRI, format="ntriples")

print(ONTOLOGY, ONTOLOGY_PATH)
save_ontology(ONTOLOGY, ONTOLOGY_PATH)
save_levels_dependencies()

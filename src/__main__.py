"""Main file"""
from src import config

with config.ONTOLOGY as onto:

    onto.save(file="cognitio", format="rdfxml")

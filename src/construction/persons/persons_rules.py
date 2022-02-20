"""SWRL Rules"""
from owlready2 import Imp

from src.builder import ONTOLOGY

with ONTOLOGY:
    imp = Imp()

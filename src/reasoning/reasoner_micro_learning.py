"""Use of Pellet or Hermit reasoners"""
from owlready2 import sync_reasoner

from src.builder import ONTOLOGY

with ONTOLOGY:
    sync_reasoner(debug=0)

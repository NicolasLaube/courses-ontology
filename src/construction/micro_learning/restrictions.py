"""Restrictions"""
import owlready2 as owl  # type: ignore

from src.builder import ONTOLOGY
from src.construction.micro_learning.classes import Anecdote, Complement, Example

with ONTOLOGY:
    owl.AllDisjoint([Complement, Example, Anecdote])

"""Restrictions"""
import owlready2 as owl  # type: ignore

from src import config
from src.construction.micro_learning.classes import Anecdote, Complement, Example

with config.ONTOLOGY as onto:
    owl.AllDisjoint([Complement, Example, Anecdote])

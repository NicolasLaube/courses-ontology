"""Restrictions"""
import owlready2 as owl

from src import config
from src.construction.micro_learning.classes import Complement, Example, Anecdote

with config.ONTOLOGY as onto:
    owl.AllDisjoint([Complement, Example, Anecdote])

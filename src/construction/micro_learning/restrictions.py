"""Restrictions"""
# import owlready2 as owl

from src import config
from src.construction.micro_learning.classes import Fragment

with config.ONTOLOGY as onto:

    # Fragment types
    complement = Fragment()
    example = Fragment()
    anecdote = Fragment()

    # Restrict fragment types
    # Fragment is defined by extension, i.e. by listing its
    # Instances rather than defining its properties
    Fragment.is_a.append(onto.one_of(complement, example, anecdote))

"""Data properties"""
import owlready2 as owl

from src import config

with config.ONTOLOGY as onto:

    class is_title(owl.Property):
        """Title"""

        ontology = onto
        range = [str]

    class is_description(owl.Property):
        """Description"""

        ontology = onto
        range = [str]

    class is_content(owl.Property):
        """Content"""

        ontology = onto
        range = [str]

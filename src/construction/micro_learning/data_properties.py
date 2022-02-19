"""Data properties"""
import owlready2 as owl  # type: ignore

from src import config

with config.ONTOLOGY as onto:

    class is_title(owl.DataProperty):
        """Title"""

        ontology = onto
        range = [str]

    class is_description(owl.DataProperty):
        """Description"""

        ontology = onto
        range = [str]

    class is_content(owl.DataProperty):
        """Content"""

        ontology = onto
        range = [str]

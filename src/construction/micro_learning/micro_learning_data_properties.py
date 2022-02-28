"""Data properties"""
from owlready2 import DataProperty, FunctionalProperty  # type: ignore

from src.builder import ONTOLOGY, Time

with ONTOLOGY:

    class is_title(DataProperty, FunctionalProperty):
        """Title"""

        range = [str]

    class is_description(DataProperty):
        """Description"""

        range = [str]

    class is_content(DataProperty):
        """Content"""

        range = [str]

    class lasts(DataProperty, FunctionalProperty):
        """Duration"""

        range = [Time]

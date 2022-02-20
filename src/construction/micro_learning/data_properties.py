"""Data properties"""
from owlready2 import DataProperty  # type: ignore

from src.builder import ONTOLOGY, Time

with ONTOLOGY:

    class is_title(DataProperty):
        """Title"""

        range = [str]

    class is_description(DataProperty):
        """Description"""

        range = [str]

    class is_content(DataProperty):
        """Content"""

        range = [str]

    class lasts(DataProperty):
        """Duration"""

        range = [Time]

"""
Micro learning courses properties
"""
import owlready2 as owl

from src import config
from src.construction.micro_learning.classes import Course, Knowledge, Module, Thematic

with config.ONTOLOGY as onto:

    class is_in_thematic(owl.ObjectProperty):
        """Course X is in Thematic Y"""

        ontology = onto
        domain = [Course]
        range = [Thematic]

    class has_as_course(owl.ObjectProperty):
        """Course X is from Thematic Y"""

        ontology = onto
        domain = [Thematic]
        range = [Course]
        inverse_property = is_in_thematic

    class is_in_course(owl.ObjectProperty):
        """Module X is in Course Y"""

        ontology = onto
        domain = [Module]
        range = [Course]

    class has_as_module(owl.ObjectProperty):
        """Course X has as Module Y"""

        ontology = onto
        domain = [Course]
        range = [Module]
        inverse_property = is_in_course

    class is_in_module(owl.ObjectProperty):
        """Knowledge X is in Module Y"""

        ontology = onto
        domain = [Knowledge]
        range = [Module]

    class contains_knowledge(owl.ObjectProperty):
        """Module X contains Knowledge Y"""

        ontology = onto
        domain = [Knowledge]
        range = [Module]
        inverse_property = is_in_module

    class requires_module(owl.ObjectProperty):
        """Module X requires module Y"""

        ontology = onto
        domain = [Module]
        range = [Module]

    class is_required_by_modules(owl.ObjectProperty):
        """Module X is required by module by module Y"""

        ontology = onto
        domain = [Module]
        range = [Module]
        inverse_property = requires_module

    class follows_knowledge(owl.ObjectProperty):
        """Knowledge X follows knowledge Y"""

        ontology = onto
        domain = [Knowledge]
        range = [Knowledge]

    class is_followed_by_knowledge(owl.ObjectProperty):
        """Knwoledge X is followed by knwoledge Y"""

        ontology = onto
        domain = [Knowledge]
        range = [Knowledge]
        inverse_property = follows_knowledge

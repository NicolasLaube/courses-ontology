"""
Micro learning courses properties
"""
import owlready2 as owl

from src import config
from src.micro_learning.classes import Course, Fragment, Knowledge, Module, Thematic

with config.ONTOLOGY as onto:

    class is_course_in_thematic(owl.Property):
        """Course X is in Thematic Y"""

        ontology = onto
        domain = [Course]
        range = [Thematic]

    class has_as_course(owl.Property):
        """Course X is from Thematic Y"""

        ontology = onto
        domain = [Thematic]
        range = [Course]
        inverse_property = is_course_in_thematic

    class is_module_in_course(
        owl.FunctionalProperty
    ):  # Each module is in one course only
        """Module X is in Course Y"""

        ontology = onto
        domain = [Module]
        range = [Course]

    class has_as_module(owl.FunctionalProperty):  # Each module is in one course only
        """Course X has as Module Y"""

        ontology = onto
        domain = [Course]
        range = [Module]
        inverse_property = is_module_in_course

    class is_knowledge_in_module(owl.Property):
        """Knowledge X is in Module Y"""

        ontology = onto
        domain = [Knowledge]
        range = [Module]

    class contains_knowledge(owl.Property):
        """Module X contains Knowledge Y"""

        ontology = onto
        domain = [Knowledge]
        range = [Module]
        inverse_property = is_knowledge_in_module

    class is_associated_with_knowledge(owl.Property):
        """Fragment X is associated with Knwoledge Y"""

        ontology = onto
        domain = [Fragment]
        range = [Knowledge]

    class can_be_presented_as(owl.Property):
        """Knowledge X can be presented as a Fragment Y"""

        ontology = onto
        domain = [Knowledge]
        range = [Fragment]

    class module_is_followed_by(owl.Property):
        """Defines the order of modules"""

        ontology = onto
        domain = [Module]
        range = [Module]

    class module_is_preceeded_by(owl.Property):
        """Defines the order of modules"""

        ontology = onto
        domain = [Module]
        range = [Module]
        inverse_property = module_is_followed_by

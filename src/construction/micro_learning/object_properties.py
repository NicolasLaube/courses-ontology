"""
Micro learning courses properties
"""
# pylint: disable=E0102
from owlready2 import Thing  # type: ignore

from src.builder import ONTOLOGY
from src.construction.micro_learning.classes import Course, Knowledge, Module, Thematic

with ONTOLOGY:

    class is_in_thematic(Course >> Thematic):  # type: ignore
        """Course X is in Thematic Y"""

    class Course(Thing):  # type: ignore
        """
        Courses class (which must have at least one thematic)
        ---
        For example 'The pop' is a course
        """

        # Forward declaration (A course must have at least one thematic)
        # Class isn't overwritten but completed
        is_in_thematic = Thematic

    class has_as_course(Thematic >> Course):  # type: ignore
        """Course X is from Thematic Y"""

        inverse_property = is_in_thematic

    class is_in_course(Module >> Course):  # type: ignore
        """Module X is in Course Y"""

    class has_as_module(Course >> Module):  # type: ignore
        """Course X has as Module Y"""

        inverse_property = is_in_course

    class is_in_module(Knowledge >> Module):  # type: ignore
        """Knowledge X is in Module Y"""

    class contains_knowledge(Module >> Knowledge):  # type: ignore
        """Module X contains Knowledge Y"""

        inverse_property = is_in_module

    class requires_module(Module >> Module):  # type: ignore
        """Module X requires module Y"""

    class is_required_by_modules(Module >> Module):  # type: ignore
        """Module X is required by module by module Y"""

        inverse_property = requires_module

    class follows_knowledge(Knowledge >> Knowledge):  # type: ignore
        """Knowledge X follows knowledge Y"""

    class is_followed_by_knowledge(Knowledge >> Knowledge):  # type: ignore
        """Knwoledge X is followed by knwoledge Y"""

        inverse_property = follows_knowledge

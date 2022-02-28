"""Persons onject properties"""
# pylint: disable=E0102
from owlready2 import AllDisjoint

from src.builder import ONTOLOGY
from src.construction.micro_learning.micro_learning_classes import Course, Module
from src.construction.persons.persons_classes import Person

with ONTOLOGY:

    class created_course(Person >> Course):  # type: ignore
        """Person X created Course Y"""

    class course_was_created_by(Course >> Person):  # type: ignore
        """Course X was create by person Y"""

        inverse_property = created_course

    class created_module(Person >> Module):  # type: ignore
        """Person X created Module Y"""

    class module_was_created_by(Module >> Person):  # type: ignore
        """Module X was create by person Y"""

        inverse_property = created_module

    class reviewed(Person >> Module):  # type: ignore
        """Person X reviewed Course or Module Y"""

    class was_reviewed_by(Module >> Person):  # type: ignore
        """Course or Module X was reviewed by person Y"""

        inverse_property = reviewed

    class finished_course(Person >> Course):  # type: ignore
        """Person X finished Course"""

    class course_was_finished_by(Course >> Person):  # type: ignore
        """Course X has as Course Y"""

        inverse_property = finished_course

    class finished_module(Person >> Module):  # type: ignore
        """Person X finished Module"""

    class module_was_finished_by(Module >> Person):  # type: ignore
        """Course X has as Module Y"""

        inverse_property = finished_module

    class started_course(Person >> Course):  # type: ignore
        """Person X started Course Y"""

    class started_module(Person >> Module):  # type: ignore
        """Person X started Module Y"""

    class failed(Person >> Module):  # type: ignore
        """Person X failed module Y"""

    class was_failed_by(Module >> Person):  # type: ignore
        """Module X was failed by person Y"""

        inverse_property = failed

    class follows(Person >> Person):  # type: ignore
        """Person X follows Person Y"""

    class is_followed_by(Person >> Person):  # type: ignore
        """Person X is followed by Person Y"""

        inverse_property = follows

    AllDisjoint([ONTOLOGY.failed, ONTOLOGY.finished_module])

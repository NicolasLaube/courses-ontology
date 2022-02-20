"""Persons onject properties"""
# pylint: disable=E0102
from src.builder import ONTOLOGY
from src.construction.micro_learning.classes import Course, Knowledge
from src.construction.persons.persons_classes import Person

with ONTOLOGY:

    class created_course(Person >> Course):  # type: ignore
        """Person X created Course Y"""

    class was_created_by(Course >> Person):  # type: ignore
        """Course X was create by person Y"""

        inverse_property = created_course

    class finished(Person >> Course):  # type: ignore
        """Person X finished Module or Course"""

    class was_finished_by(Course >> Person):  # type: ignore
        """Course X has as Module Y"""

        inverse_property = finished

    class was_acquired_by(Knowledge >> Person):  # type: ignore
        """Knowledge X is in Module Y"""

    class acquired_knowledge(Person >> Knowledge):  # type: ignore
        """Module X contains Knowledge Y"""

        inverse_property = was_acquired_by

    class has_access_to(Person >> Course):  # type: ignore
        """Module X requires module Y"""

    class is_accessible_to(Course >> Person):  # type: ignore
        """Module X is required by module by module Y"""

        inverse_property = has_access_to

    class follows(Person >> Person):  # type: ignore
        """Person X follows Person Y"""

    class is_followed_by(Person >> Person):  # type: ignore
        """Person X is followed by Person Y"""

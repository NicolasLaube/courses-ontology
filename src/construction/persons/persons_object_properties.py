"""Persons onject properties"""
# pylint: disable=E0102
from owlready2 import ObjectProperty

from src.builder import ONTOLOGY
from src.construction.micro_learning.classes import Course, Knowledge, Module
from src.construction.persons.persons_classes import Person

with ONTOLOGY:

    class created(ObjectProperty):  # type: ignore
        """Person X created Course or Module Y"""

        domain = [Module, Course]
        range = [Person]

    class was_created_by(ObjectProperty):  # type: ignore
        """Course or Module X was create by person Y"""

        domain = [Module, Course]
        range = [Person]
        inverse_property = created

    class finished(ObjectProperty):  # type: ignore
        """Person X finished Module or Course"""

        domain = [Person]
        range = [Module, Course]

    class was_finished_by(ObjectProperty):  # type: ignore
        """Course X has as Module Y"""

        domain = [Module, Course]
        range = [Person]
        inverse_property = finished

    class started(ObjectProperty):
        """Person X started Module or Course Y"""

        domain = [Person]
        range = [Module, Course]

    class failed(Person >> Module):  # type: ignore
        """Person X failed module Y"""

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

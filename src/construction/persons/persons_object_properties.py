"""Persons onject properties"""
# pylint: disable=E0102
from owlready2 import ObjectProperty

from src.builder import ONTOLOGY
from src.construction.micro_learning.classes import Course, Module
from src.construction.persons.persons_classes import Person

with ONTOLOGY:

    class created(ObjectProperty):
        """Person X created Course or Module Y"""

        domain = [Module, Course]
        range = [Person]

    class was_created_by(ObjectProperty):
        """Course or Module X was create by person Y"""

        domain = [Module, Course]
        range = [Person]
        inverse_property = created

    class reviewed(ObjectProperty):
        """Person X reviewed Course or Module Y"""

        domain = [Module, Course]
        range = [Person]

    class was_reviewed_by(ObjectProperty):
        """Course or Module X was reviewed by person Y"""

        domain = [Module, Course]
        range = [Person]
        inverse_property = created

    class finished(ObjectProperty):
        """Person X finished Module or Course"""

        domain = [Person]
        range = [Module, Course]

    class was_finished_by(ObjectProperty):
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

    class was_failed_by(Module >> Person):  # type: ignore
        """Module X was failed by person Y"""

        inverse_property = failed

    class follows(Person >> Person):  # type: ignore
        """Person X follows Person Y"""

    class is_followed_by(Person >> Person):  # type: ignore
        """Person X is followed by Person Y"""

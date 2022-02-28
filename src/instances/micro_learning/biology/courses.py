"""Biology courses"""

from src.builder import ONTOLOGY
from src.construction.micro_learning.micro_learning_classes import Course
from src.instances.micro_learning.thematics import biology

with ONTOLOGY:
    microbiota = Course("Microbiota")
    theory_of_evolution = Course("TheoryOfEvolution")

    biology_courses = [microbiota, theory_of_evolution]

    biology.has_as_course.extend(biology_courses)

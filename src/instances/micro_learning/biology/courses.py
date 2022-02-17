"""Biology courses"""

from src.construction.micro_learning.classes import Course
from src.instances.micro_learning.thematics import biology

microbiota = Course("Microbiota")
theory_of_evolution = Course("TheoryOfEvolution")

biology_courses = [microbiota, theory_of_evolution]

biology.has_as_course.extend(biology_courses)

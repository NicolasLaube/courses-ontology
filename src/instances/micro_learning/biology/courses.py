"""Biology courses"""

from src.construction.micro_learning.classes import Course
from src.instances.micro_learning.thematics import biology

micorbiota = Course("Micorbiota")
theory_of_evolution = Course("TheoryOfEvolution")

biology_courses = [micorbiota, theory_of_evolution]

biology.has_a_course.extend(biology_courses)

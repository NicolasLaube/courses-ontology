"""Music courses"""
from src.builder import ONTOLOGY
from src.construction.micro_learning.classes import Course
from src.instances.micro_learning.thematics import music

with ONTOLOGY:
    pop_music = Course("PopMusic")
    classical_music = Course("ClassicalMusic")
    rock_music = Course("RockMusic")

    music_courses = [pop_music, classical_music, rock_music]

    music.has_as_course.extend(music_courses)

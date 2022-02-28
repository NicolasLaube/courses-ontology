"""Music courses"""
from owlready2 import locstr

from src.builder import ONTOLOGY
from src.construction.micro_learning.micro_learning_classes import Course
from src.instances.micro_learning.thematics import music

with ONTOLOGY:
    pop_music = Course("PopMusic")
    classical_music = Course("ClassicalMusic")
    rock_music = Course("RockMusic")

    music_courses = [pop_music, classical_music, rock_music]

    music.has_as_course.extend(music_courses)

    pop_music.label = [
        locstr("La musique pop", "fr"),
        locstr("Die Popmusik", "de"),
        locstr("The pop music", "en"),
        locstr("Musica pop", "es"),
    ]

    pop_music.comment = [
        locstr(
            "Ce cours présente l'évolution de la musique pop depuis\
                 son apparition jusqu'à aujourd'hui.",
            "fr",
        ),
        locstr(
            "Dieser Kurs präsentiert die Entwicklung der Popmusik seit\
                  seine Erscheinung bis heute.",
            "de",
        ),
        locstr(
            "This course presents the evolution of pop music since\
                  its appearance until today.",
            "en",
        ),
        locstr(
            "Este curso presenta la evolución de la música pop desde\
                  su aparición hasta hoy.",
            "es",
        ),
    ]

    rock_music.label = [
        locstr("La musique rock", "fr"),
        locstr("Die Rockmusik", "de"),
        locstr("The rock music", "en"),
        locstr("La música rock", "es"),
    ]

    classical_music.label = [
        locstr("Histoire de la musique classique", "fr"),
        locstr("Geschichte der klassischen Musik", "de"),
        locstr("History of classical music", "en"),
        locstr("Historia de la musica clasica", "es"),
    ]

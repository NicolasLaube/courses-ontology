"""Execution of all requests"""
from pprint import pprint

from src.builder import ONTOLOGY
from src.requests.requests_micro_learning import (
    get_all_courses,
    get_all_thematics,
    get_course_knowledge,
    get_course_modules,
    get_course_thematics,
    get_module_knowledge,
    get_prerequisites,
    get_unlocked_modules,
)

with ONTOLOGY:

    print("\nGet all thematics: ")
    print(get_all_thematics())
    print("\nGet all courses: ")
    pprint(get_all_courses())
    print("\nThematics of course Pop music: ")
    pprint(get_course_thematics(ONTOLOGY.PopMusic))
    print("\nModules of course Pop music: ")
    pprint(get_course_modules(ONTOLOGY.PopMusic))
    print("\nKnowledge of course Pop music: ")
    pprint(get_course_knowledge(ONTOLOGY.PopMusic))
    print("\nKnowledge of module Beatles: ")
    pprint(get_module_knowledge(ONTOLOGY.Beatles))
    print("\nPrerequisites of modules Beatles: ")
    pprint(get_prerequisites(ONTOLOGY.Beatles))
    print("\nUnlocked modules of Beatles: ")
    print(ONTOLOGY.Antoine)
    pprint(get_unlocked_modules(ONTOLOGY.PopMusicFamousArtists, ONTOLOGY.Nicolas))

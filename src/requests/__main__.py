"""Execution of all requests"""
from pprint import pprint

from src.builder import ONTOLOGY
from src.requests.requests_micro_learning import (
    get_all_courses,
    get_all_thematics,
    get_course_knowledge,
    get_course_modules,
    get_course_prerequisites,
    get_course_thematics,
    get_module_knowledge,
    get_module_prerequisites,
)
from src.requests.requests_persons import (  # get_learner_accessible_courses,
    get_course_creators,
    get_course_finishers,
    get_learner_knowledge,
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
    print("\nPrerequisites of modules PopMusicFamousArtists: ")
    pprint(get_module_prerequisites(ONTOLOGY.PopMusicFamousArtists))
    print("\nPrerequisites of course RockMusic: ")
    pprint(get_course_prerequisites(ONTOLOGY.RockMusic))

    print("\n\n# Requests on learners")
    print("\nFinishers of course PopMusic:")
    pprint(get_course_finishers(ONTOLOGY.PopMusic))
    print("\nCreators of course PopMusic:")
    pprint(get_course_creators(ONTOLOGY.PopMusic))
    print("\nMathilde's unlocked modules of PopMusicFamousArtists:")
    pprint(get_unlocked_modules(ONTOLOGY.PopMusicFamousArtists, ONTOLOGY.Mathilde))
    print("\nGet Mathilde's Knwoledge:")
    pprint(get_learner_knowledge(ONTOLOGY.Mathilde))
    print("\nGeorge's accessible courses:")
    # pprint(get_learner_accessible_courses(ONTOLOGY.George))

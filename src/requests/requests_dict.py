"""Requests dict"""
from src.requests.requests_micro_learning import (
    get_all_courses,
    get_all_thematics,
    get_course_knowledge,
    get_course_thematics,
    get_course_modules,
    get_module_knowledge,
    get_module_prerequisites,
    get_course_prerequisites,
)
from src.requests.requests_persons import (
    get_course_creators,
    get_course_finishers,
    get_learner_knowledge,
    get_learner_accessible_courses,
    get_modules_to_revise,
    get_number_finishers,
    get_number_starters,
    get_unlocked_modules,
)

SPARQL_REQUESTS = {
    "Thematics": get_all_thematics,
    "Courses": get_all_courses,
    "Modules of course": get_course_modules,
    "Knowledge of module": get_module_knowledge,
    "Knowledge of course": get_course_knowledge,
    "Thematic of course": get_course_thematics,
    "Module prerequesites": get_module_prerequisites,
    "Course prerequesites": get_course_prerequisites,
    "Module unlocked by user": get_unlocked_modules,
    "Course finishers": get_course_finishers,
    "Course creators": get_course_creators,
    "Learner knowledge": get_learner_knowledge,
    "Accessible courses for learner": get_learner_accessible_courses,
    "Modules to revise": get_modules_to_revise,
    "Number starters": get_number_starters,
    "Number finishers": get_number_finishers,
}

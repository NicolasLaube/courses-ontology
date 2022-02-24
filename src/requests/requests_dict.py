"""Requests dict"""
from src.requests.requests_micro_learning import (
    get_all_courses,
    get_all_thematics,
    get_course_knowledge,
    get_course_modules,
    get_module_knowledge,
    get_prerequisites,
)
from src.requests.requests_persons import (
    get_course_creators,
    get_course_finishers,
    get_learner_knowledge,
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
    "Module prerequesites": get_prerequisites,
    "Module unlocked by module": get_unlocked_modules,
    "Course finishers": get_course_finishers,
    "Course creators": get_course_creators,
    "Learner knowledge": get_learner_knowledge,
    "Modules to revise": get_modules_to_revise,
    "Number starters": get_number_starters,
    "Number finishers": get_number_finishers,
}

"""All functions for reasoning with Prolog"""

import os
import json
from pyswip import Prolog
from src.reasoner.utils import (
    export_predicated_to_prolog,
    pyswip_output_to_str,
)
from src import ontology
from src.requests import get_all_courses

GRAPH_LEVELS_PATH = os.path.join("storage", "graph_levels.json")
MIN_DEPENDENCIES_PATH = os.path.join("storage", "min_dependencies.json")

prolog = Prolog()

export_predicated_to_prolog(ontology, prolog)

prolog.consult("./src/reasoner/rules.pl")


def get_module_level(module, course):
    """To get the graph level of a module in a specific course"""
    command = f"module_level_in_course('{module}', '{course}', Level)"
    results = prolog.query(command)
    return list(results)[0]["Level"]


def get_all_dependencies(module, course):
    """To get all the dependencies of a module in a specific course"""
    command = f"get_all_dependencies('{module}', '{course}', Dependencies)"
    results = prolog.query(command)
    return [pyswip_output_to_str(dep) for dep in list(results)[0]["Dependencies"]]


def get_min_dependencies(module, course):
    """To get the minimal dependencies of a module in a specific course"""
    command = f"get_min_dependencies('{module}', '{course}', Dependencies)"
    results = prolog.query(command)
    return [pyswip_output_to_str(dep) for dep in list(results)[0]["Dependencies"]]


def get_all_modules_in_course(course):
    """To get all the modules of a specific course"""
    command = f"find_course_modules('{course}', [], CourseModules)"
    results = prolog.query(command)
    return [pyswip_output_to_str(dep) for dep in list(results)[0]["CourseModules"]]


def get_module_levels_in_course(course):
    """To get the graph level of all the modules of a specific course"""
    command = f"get_all_levels_for_course('{course}', AllLevels)"
    results = prolog.query(command)
    results_str = list(results)[0]["AllLevels"]
    tab_res = results_str.split(")")[-2].split("(")[-1].split(",")[1:]
    table_modules = [
        pyswip_output_to_str(x.strip()) for i, x in enumerate(tab_res) if i % 2 == 1
    ]
    table_levels = [int(x.strip()) for i, x in enumerate(tab_res) if i % 2 == 0]
    dict_merged_levels = {}
    for level, name in zip(table_levels, table_modules):
        dict_merged_levels[name] = level
    return dict_merged_levels


def get_min_dependencies_in_course(course):
    """To get all the minimal dependencies of the modules of a specific course"""
    # There is a prolog command to get the dependencies more simply, but pyswip doesn't send back
    # the results in an operable format

    # First we must get the course levels
    dict_levels = get_module_levels_in_course(course)
    dict_levels_str = f"dict{json.dumps(dict_levels)}".replace('"', "'")

    # Then we get all the modules of the course
    command_all_modules = f"find_course_modules('{course}', [], List)"
    results_all_modules = list(prolog.query(command_all_modules))[0]["List"]
    all_modules_str = [pyswip_output_to_str(x) for x in results_all_modules]

    # Finally, for all the modules, we get its min dependencies
    all_min_dependencies = {}
    for module_str in all_modules_str:
        command_dependencies = f"get_min_dependencies_optimized('{module_str}', '{course}',\
                                {dict_levels_str}, MinDependenciesX)"
        result_dependencies = prolog.query(command_dependencies)
        min_dependencies = [
            pyswip_output_to_str(dep)
            for dep in list(result_dependencies)[0]["MinDependenciesX"]
        ]
        all_min_dependencies[pyswip_output_to_str(module_str)] = min_dependencies
    return all_min_dependencies


def save_levels_dependencies():
    """To save levels and min dependencies in a json file"""
    courses = get_all_courses()
    courses = [course[0].name for course in courses]
    all_levels = {}
    all_dependencies = {}
    for course in courses:
        all_levels[course] = get_module_levels_in_course(course)
        all_dependencies[course] = get_min_dependencies_in_course(course)
    with open(GRAPH_LEVELS_PATH, "w", encoding="utf-8") as file:
        json.dump(all_levels, file)
    with open(MIN_DEPENDENCIES_PATH, "w", encoding="utf-8") as file:
        json.dump(all_dependencies, file)

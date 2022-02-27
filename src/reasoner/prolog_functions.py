"""All functions for reasoning with Prolog"""

import json
from pyswip import Prolog
from src.reasoner.utils import (
    export_predicated_to_prolog,
    pyswip_output_to_str,
    pyswip_to_onto,
)
from src import ontology

prolog = Prolog()

export_predicated_to_prolog(ontology, prolog)

prolog.consult("./src/reasoner/rules.pl")


def get_module_level(module, course):
    """To get the graph level of a module in a specific course"""
    command = f"module_level_in_course('{module.name}', '{course.name}', Level)"
    results = prolog.query(command)
    return list(results)[0]["Level"]


def get_all_dependencies(module, course):
    """To get all the dependencies of a module in a specific course"""
    command = f"get_all_dependencies('{module.name}', '{course.name}', Dependencies)"
    results = prolog.query(command)
    return [pyswip_to_onto(ontology, dep) for dep in list(results)[0]["Dependencies"]]


def get_min_dependencies(module, course):
    """To get the minimal dependencies of a module in a specific course"""
    command = f"get_min_dependencies('{module.name}', '{course.name}', Dependencies)"
    results = prolog.query(command)
    return [pyswip_to_onto(ontology, dep) for dep in list(results)[0]["Dependencies"]]


def get_module_levels_in_course(course):
    """To get the graph level of all the modules of a specific course"""
    command = f"get_all_levels_for_course('{course.name}', AllLevels)"
    results = prolog.query(command)
    results_str = list(results)[0]["AllLevels"]
    tab_res = results_str.split(")")[-2].split("(")[-1].split(",")[1:]
    table_entities = [
        pyswip_to_onto(ontology, x.strip()) for i, x in enumerate(tab_res) if i % 2 == 1
    ]
    table_levels = [int(x.strip()) for i, x in enumerate(tab_res) if i % 2 == 0]
    if len(table_levels) > 0:
        max_level = max(table_levels)
        table_merged_levels = [[] for _ in range(max_level + 1)]
        for level, entity in zip(table_levels, table_entities):
            table_merged_levels[level].append(entity)
        return table_merged_levels
    else:
        return []


def get_min_dependencies_in_course(course):
    """To get all the minimal dependencies of the modules of a specific course"""
    # There is a prolog command to get the dependencies more simply, but pyswip doesn't send back
    # the results in an operable format

    # First we must get the course levels
    command_levels = f"get_all_levels_for_course('{course.name}', AllLevels)"
    results_levels = prolog.query(command_levels)
    results_levels_str = list(results_levels)[0]["AllLevels"]
    tab_levels_res = results_levels_str.split(")")[-2].split("(")[-1].split(",")[1:]
    table_levels_names = [
        pyswip_output_to_str(x.strip())
        for i, x in enumerate(tab_levels_res)
        if i % 2 == 1
    ]
    table_levels_levels = [
        int(x.strip()) for i, x in enumerate(tab_levels_res) if i % 2 == 0
    ]
    dict_levels = {}
    for level, name in zip(table_levels_levels, table_levels_names):
        dict_levels[name] = level
    dict_levels_str = f"dict{json.dumps(dict_levels)}".replace('"', "'")

    # Then we get all the modules of the course
    command_all_modules = f"find_course_modules('{course.name}', [], List)"
    results_all_modules = list(prolog.query(command_all_modules))[0]["List"]
    all_modules_str = [pyswip_output_to_str(x) for x in results_all_modules]

    # Finally, for all the modules, we get its min dependencies
    all_min_dependencies = {}
    for module_str in all_modules_str:
        command_dependencies = f"get_min_dependencies_optimized('{module_str}', '{course.name}',\
                                {dict_levels_str}, MinDependenciesX)"
        result_dependencies = prolog.query(command_dependencies)
        min_dependencies = [
            pyswip_to_onto(ontology, dep)
            for dep in list(result_dependencies)[0]["MinDependenciesX"]
        ]
        all_min_dependencies[pyswip_to_onto(ontology, module_str)] = min_dependencies
    return all_min_dependencies

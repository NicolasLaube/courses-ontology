"""All functions for reasoning with Prolog"""

from pyswip import Prolog
from src.reasoner.utils import export_predicated_to_prolog
from src import ontology

prolog = Prolog()

export_predicated_to_prolog(ontology, prolog)

prolog.consult("./src/prolog/rules.pl")


def get_module_level(module, course):
    """To get the graph level of a module in a specific course"""
    command = f"module_level_in_course('{module}', '{course}', Level)"
    results = prolog.query(command)
    return list(results)[0]["Level"]


def get_all_dependencies(module, course):
    """To get all the dependencies of a module in a specific course"""
    command = f"get_all_dependencies('{module}', '{course}', Dependencies)"
    results = prolog.query(command)
    return list(results)[0]["Dependencies"]


def get_min_dependencies(module, course):
    """To get the minimal dependencies of a module in a specific course"""
    command = f"get_min_dependencies('{module}', '{course}', Dependencies)"
    results = prolog.query(command)
    return list(results)[0]["Dependencies"]


print(get_module_level("WomenInRockMusic", "RockMusic"))
print(get_all_dependencies("MicrobiotaMetaGenomicStudy", "Microbiota"))
print(get_min_dependencies("MicrobiotaMetaGenomicStudy", "Microbiota"))

# print(
#     pyswip_to_str(
#         prolog.query(
#             "find_req_modules_with_course('WomenInRockMusic', 'RockMusic', [], List)"
#         )
#     )
# )

# print(
#     pyswip_to_str(
#         prolog.query("module_level_in_course('WomenInRockMusic', 'RockMusic', N)")
#     )
# )

# print(
#     pyswip_to_str(
#         prolog.query(
#             "find_req_modules_with_course('PopMusicBandsAndTheirFans', 'PopMusic', [], List)"
#         )
#     )
# )

# print(
#     pyswip_to_str(
#         prolog.query(
#             "get_all_dependencies('MicrobiotaMetaGenomicStudy', 'Microbiota', List)"
#         )
#     )
# )

# print(
#     pyswip_to_str(
#         prolog.query("get_min_dependencies('PopMusicNineties', 'PopMusic', List)")
#     )
# )

# print(
#     pyswip_to_str(
#         prolog.query("filter_list(['f', 'b', 'a', 'f', 'g'], ['a', 'c'], List)")
#     )
# )

# print(
#     pyswip_to_str(
#         prolog.query(
#             "get_all_dependencies_from_list(['PopMusicPresentation'], 'PopMusic', List)"
#         )
#     )
# )


# print(pyswip_to_str(prolog.query("memberCheckSimple(['a', 'b', 'c'], 'd')")))

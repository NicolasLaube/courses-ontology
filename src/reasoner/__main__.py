from src.reasoner import (
    get_module_level,
    get_all_dependencies,
    get_min_dependencies,
    get_module_levels_in_course,
    get_min_dependencies_in_course,
)

print(
    get_module_level(
        "WomenInRockMusic",
        "RockMusic",
    )
)
print(
    get_all_dependencies(
        "MicrobiotaMetaGenomicStudy",
        "Microbiota",
    )
)
print(
    get_min_dependencies(
        "MicrobiotaMetaGenomicStudy",
        "Microbiota",
    )
)
print(get_module_levels_in_course("RockMusic"))
print(get_min_dependencies_in_course("RockMusic"))

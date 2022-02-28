from src.reasoner import (
    get_module_level,
    get_all_dependencies,
    get_min_dependencies,
    get_all_modules_in_course,
    get_module_levels_in_course,
    get_min_dependencies_in_course,
)

print("\nModule level for module WomenInRockMusic:")
print(
    get_module_level(
        "WomenInRockMusic",
        "RockMusic",
    )
)

print("\nAll dependencies for module MicrobiotaMetaGenomicStudy:")
print(
    get_all_dependencies(
        "MicrobiotaMetaGenomicStudy",
        "Microbiota",
    )
)

print("\nMin dependencies for module MicrobiotaMetaGenomicStudy:")
print(
    get_min_dependencies(
        "MicrobiotaMetaGenomicStudy",
        "Microbiota",
    )
)

print("\nAll modules of course Microbiota:")
print(get_all_modules_in_course("Microbiota"))

print("\nAll levels in course RockMusic:")
print(get_module_levels_in_course("RockMusic"))

print("\nAll min dependencies in course RockMusic:")
print(get_min_dependencies_in_course("RockMusic"))

from src.reasoner import (
    get_module_level,
    get_all_dependencies,
    get_min_dependencies,
    get_module_levels_in_course,
    get_min_dependencies_in_course,
)
from src import ontology

print(
    get_module_level(
        ontology.search_one(iri="*#WomenInRockMusic"),
        ontology.search_one(iri="*#RockMusic"),
    )
)
print(
    get_all_dependencies(
        ontology.search_one(iri="*#MicrobiotaMetaGenomicStudy"),
        ontology.search_one(iri="*#Microbiota"),
    )
)
print(
    get_min_dependencies(
        ontology.search_one(iri="*#MicrobiotaMetaGenomicStudy"),
        ontology.search_one(iri="*#Microbiota"),
    )
)
print(get_module_levels_in_course(ontology.search_one(iri="*#RockMusic")))
print(get_min_dependencies_in_course(ontology.search_one(iri="*#RockMusic")))

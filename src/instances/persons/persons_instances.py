"""Persons instances"""
from src.builder import ONTOLOGY
from src.construction import Person
from src.instances.micro_learning import (
    classical_music,
    economic_cycles,
    economy_courses,
    enterotypes,
    environment_influence_on_microbiota,
    fecal_microbiota_transplant,
    gdp,
    growth,
    human_microbiota,
    inflation,
    macroeconomy_modules,
    microbiota_composition,
    microbiota_modules,
    microbiota_presentation,
    microbiota_seasonalty,
    microbiota_structure,
    microbiota_through_life,
    national_accounts,
    phylogenetic_kernel,
    pop_music,
    pop_music_modules,
    price_index,
    rock_music,
    unemployement,
)

with ONTOLOGY:

    antoine = Person("Antoine")
    romain = Person("Romain")
    nicolas = Person("Nicolas")

    antoine.created.extend([pop_music, rock_music, classical_music])
    antoine.created.extend(pop_music_modules)

    nicolas.created.extend(economy_courses)
    nicolas.created.extend(macroeconomy_modules)

    lola = Person("Lola")

    lola.finished.extend(
        [
            gdp,
            national_accounts,
            price_index,
            unemployement,
            inflation,
            economic_cycles,
            growth,
        ]
    )
    lola.follows.append(nicolas)

    paola = Person("Paola")

    paola.finished.extend(
        [
            microbiota_presentation,
            microbiota_structure,
            microbiota_seasonalty,
            environment_influence_on_microbiota,
            fecal_microbiota_transplant,
            microbiota_composition,
            human_microbiota,
            phylogenetic_kernel,
            enterotypes,
        ]
    )

    paola.started.append(microbiota_through_life)

    mathilde = Person("Mathilde")

    mathilde.finished.extend(microbiota_modules)

    lucy = Person("Lucy")
    lea = Person("Lea")
    beatrice = Person("Beatrice")

    theo = Person("Theo")
    leo = Person("Leo")
    george = Person("George")

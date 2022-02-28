"""Persons instances"""
from src.builder import ONTOLOGY
from src.construction import Person
from src.instances.micro_learning import (
    abba,
    baroque_pop,
    beach_boys,
    beatles,
    boys_girls_bands,
    brit_pop,
    britney_spears,
    bubblegum_pop,
    classical_music,
    country_pop,
    dance_pop,
    difficulty_to_study_musical_style,
    dolly_parton,
    economic_cycles,
    economy_courses,
    enterotypes,
    environment_influence_on_microbiota,
    euro_pop,
    fecal_microbiota_transplant,
    gdp,
    growth,
    human_microbiota,
    inflation,
    madonna,
    michael_jackson,
    microbiota_composition,
    microbiota_modules,
    microbiota_presentation,
    microbiota_seasonalty,
    microbiota_structure,
    microbiota_through_life,
    national_accounts,
    phylogenetic_kernel,
    pop_music,
    pop_music_2000,
    pop_music_eighties,
    pop_music_famous_artists,
    pop_music_festivals,
    pop_music_modules,
    pop_music_nineties,
    pop_music_origin,
    pop_music_presentation,
    pop_music_seventies,
    pop_music_sixties,
    price_index,
    rock_music,
    rock_music_famous_artists,
    rock_music_festivals,
    rock_music_presentation,
    rock_n_roll_presentation,
    spice_girls,
    synthesizer_in_the_eighties,
    taylor_swift,
    unemployement,
)

with ONTOLOGY:

    antoine = Person("Antoine")
    romain = Person("Romain")
    nicolas = Person("Nicolas")

    antoine.created_course.extend([pop_music, rock_music, classical_music])
    # antoine.created_module.extend(pop_music_modules)

    nicolas.created_course.extend(economy_courses)
    # nicolas.created_module.extend(macroeconomy_modules)

    lola = Person("Lola")

    lola.finished_module.extend(
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

    paola.finished_module.extend(
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

    paola.started_module.append(microbiota_through_life)
    paola.finished_course.append(pop_music)

    mathilde = Person("Mathilde")

    mathilde.finished_module.extend(microbiota_modules)

    lucy = Person("Lucy")
    lucy.finished_module.extend(
        [
            pop_music_presentation,
            pop_music_famous_artists,
            pop_music_festivals,
            difficulty_to_study_musical_style,
            pop_music_origin,
            rock_n_roll_presentation,
            rock_music_presentation,
        ]
    )
    lucy.failed.append(pop_music_sixties)

    lea = Person("Lea")
    lea.finished_module.extend([pop_music_presentation, pop_music_famous_artists])
    lea.started_module.append(pop_music_festivals)

    beatrice = Person("Beatrice")
    beatrice.finished_module.extend(pop_music_modules)
    beatrice.finished_module.extend([rock_music_famous_artists, rock_music_festivals])
    # next module should be rock_music_origin as difficulty_to_study_musical_style
    # already defined

    theo = Person("Theo")
    # theo is exterior

    leo = Person("Leo")
    leo.finished_module.extend(
        [
            pop_music_presentation,
            pop_music_famous_artists,
            pop_music_festivals,
            difficulty_to_study_musical_style,
            pop_music_origin,
            rock_n_roll_presentation,
            rock_music_presentation,
            pop_music_sixties,
            beatles,
            pop_music_seventies,
            bubblegum_pop,
            baroque_pop,
            beach_boys,
            country_pop,
            dolly_parton,
            taylor_swift,
            euro_pop,
            abba,
            pop_music_eighties,
            synthesizer_in_the_eighties,
            dance_pop,
            michael_jackson,
            madonna,
            pop_music_nineties,
            boys_girls_bands,
            spice_girls,
            britney_spears,
            pop_music_2000,
            brit_pop,
        ]
    )

    leo.reviewed.extend([pop_music_sixties, pop_music_eighties])

    george = Person("George")

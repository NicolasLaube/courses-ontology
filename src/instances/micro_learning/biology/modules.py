"""Biology modules"""
from src.construction.micro_learning.classes import Module
from src.instances.micro_learning.biology.courses import microbiota

## Microbiota course ##

# Introduction part
microbiota_presentation = Module("MicrobiotaPresentation")
microbiota_structure = Module("MicrobiotaStructure")
microbiota_structure.requires_modules.extend([microbiota_presentation])
microbiota_seasonalty = Module("MicrobiotaSeasonalty")
microbiota_seasonalty.requires_modules.extend(
    [microbiota_presentation, microbiota_structure]
)
environment_influence_on_microbiota = Module("EnvironmentInfluenceOnMicrobiota")
environment_influence_on_microbiota.requires_modules.extend(
    [microbiota_presentation, microbiota_structure]
)
fecal_microbiota_transplant = Module("FecalMicrobiotaTransplant")
fecal_microbiota_transplant.requires_modules.extend(
    [environment_influence_on_microbiota]
)
microbiota_composition = Module("MicrobiotaComposition")
microbiota_composition.requires_modules.extend(
    [microbiota_seasonalty, environment_influence_on_microbiota]
)

# Human microbiota part
human_microbiota = Module("HumanMicrobiota")
human_microbiota.requires_modules.extend([microbiota_composition])
phylogenetic_kernel = Module("PhylogeneticKernel")
phylogenetic_kernel.requires_modules.extend([human_microbiota])
enterotypes = Module("Enterotypes")
enterotypes.requires_modules.extend([human_microbiota])
microbiota_through_life = Module("MicrobiotaThroughLife")
microbiota_through_life.requires_modules.extend(
    [phylogenetic_kernel, microbiota_through_life]
)
microbiota_during_pregnancy = Module("MicrobiotaDuringPregnancy")
microbiota_during_pregnancy.requires_modules.extend([microbiota_through_life])
microbiota_and_antibiotics = Module("MicrobiotaAndAntibiotics")
microbiota_and_antibiotics.requires_modules.extend([microbiota_through_life])
microbiota_pathologies = Module("MicrobiotaPathologies")
microbiota_pathologies.requires_modules.extend([microbiota_through_life])

# Microbiota role part
microbiota_role = Module("MicrobiotaRole")
microbiota_role.requires_modules.extend(
    [microbiota_during_pregnancy, microbiota_and_antibiotics, microbiota_pathologies]
)
microbiota_and_immune_system = Module("MicrobiotaAndImmuneSystem")
microbiota_and_immune_system.requires_modules.extend([microbiota_role])
microbiota_stimulate_immune_system = Module("MicrobiotaStimulateImmuneSystem")
microbiota_stimulate_immune_system.requires_modules.extend(
    [microbiota_and_immune_system]
)
microbiota_and_chronic_intestine_diseases = Module(
    "MicrobiotaAndChronicIntestineDiseases"
)
microbiota_and_chronic_intestine_diseases.requires_modules.extend(
    [microbiota_stimulate_immune_system]
)
microbiota_metabolic_function = Module("MicrobiotaMetabolicFunction")
microbiota_metabolic_function.requires_modules.extend([microbiota_role])
microbiota_and_obesity = Module("MicrobiotaAndObesity")
microbiota_and_obesity.requires_modules.extend([microbiota_metabolic_function])
microbiota_and_diabet = Module("MicrobiotaAndDiabet")
microbiota_and_diabet.requires_modules.extend([microbiota_and_obesity])
microbiota_and_digestion = Module("MicrobiotaAndDigestion")
microbiota_and_digestion.requires_modules.extend([microbiota_and_diabet])
microbiota_brain_intestine_axis = Module("MicrobiotaBrainIntestineAxis")
microbiota_brain_intestine_axis.requires_modules.extend([microbiota_role])
microbiota_and_brain_development = Module("MicrobiotaAndBrainDevelopment")
microbiota_and_brain_development.requires_modules.extend(
    [microbiota_brain_intestine_axis]
)
microbiota_and_autism = Module("MicrobiotaAndAutism")
microbiota_and_autism.requires_modules.extend([microbiota_and_brain_development])
microbiota_and_psychic_state = Module("MicrobiotaAndPsychicState")
microbiota_and_psychic_state.requires_modules.extend([microbiota_and_autism])

# Researches on microbiota part
researches_on_microbiota = Module("ResearchesOnMicrobiota")
researches_on_microbiota.requires_modules.extend(
    [microbiota_and_diabet, microbiota_and_digestion, microbiota_and_psychic_state]
)
microbiota_taxonomy = Module("MicrobiotaTaxonomy")
microbiota_taxonomy.requires_modules.extend([researches_on_microbiota])
microbiota_on_axenic_animals = Module("MicrobiotaOnAxenicAnimals")
microbiota_on_axenic_animals.requires_modules.extend([researches_on_microbiota])
microbiota_meta_genomic_study = Module("MicrobiotaMetaGenomicStudy")
microbiota_meta_genomic_study.requires_modules.extend([researches_on_microbiota])


microbiota_modules = [
    microbiota_presentation,
    microbiota_structure,
    microbiota_seasonalty,
    environment_influence_on_microbiota,
    fecal_microbiota_transplant,
    microbiota_composition,
    human_microbiota,
    phylogenetic_kernel,
    enterotypes,
    microbiota_through_life,
    microbiota_during_pregnancy,
    microbiota_and_antibiotics,
    microbiota_pathologies,
    microbiota_role,
    microbiota_and_immune_system,
    microbiota_stimulate_immune_system,
    microbiota_and_chronic_intestine_diseases,
    microbiota_metabolic_function,
    microbiota_and_obesity,
    microbiota_and_diabet,
    microbiota_and_digestion,
    microbiota_brain_intestine_axis,
    microbiota_and_brain_development,
    microbiota_and_autism,
    microbiota_and_psychic_state,
    researches_on_microbiota,
    microbiota_taxonomy,
    microbiota_on_axenic_animals,
    microbiota_meta_genomic_study,
]

# Relations

microbiota.has_a_module.extend(microbiota_modules)

"""Biology modules"""
from src.construction.micro_learning.classes import Module
from src.instances.micro_learning.music.courses import pop_music

## Pop music course ##

# Introduction part
pop_music_presentation = Module("PopMusicPresentation")
pop_music_famous_artists = Module("PopMusicFamousArtists")
pop_music_famous_artists.requires_modules.extend(["pop_music_presentation"])
pop_music_festivals = Module("PopMusicFestivals")
pop_music_festivals.requires_modules.extend([pop_music_famous_artists])
difficulty_to_study_musical_style = Module("DifficultyToStudyMusicalStyle")
difficulty_to_study_musical_style.requires_modules.extend([pop_music_presentation])

# History of pop music
pop_music_origin = Module("PopMusicOrigin")
pop_music_origin.requires_modules.extend([pop_music_festivals])
rock_n_roll_presentation = Module("RockNRollPresentation")
rock_n_roll_presentation.requires_modules.extend([rock_n_roll_presentation])
rock_presentation = Module("RockPresentation")
rock_presentation.requires_modules.extend([rock_n_roll_presentation])
pop_music_sixties = Module("PopMusicSixties")
pop_music_sixties.requires_modules.extend([rock_n_roll_presentation])
beatles = Module("Beatles")
beatles.requires_modules.extend([pop_music_sixties])
pop_music_seventies = Module("PopMusicSeventies")
pop_music_seventies.requires_modules.extend([pop_music_sixties])
bubblegom_pop = Module("BubblegumPop")
bubblegom_pop.requires_modules.extend([pop_music_seventies])
baroque_pop = Module("BaroquePop")
baroque_pop.requires_modules.extend([pop_music_seventies])
beach_boys = Module("BeachBoys")
beach_boys.requires_modules.extend([baroque_pop])
country_pop = Module("CountryPop")
country_pop.requires_modules.extend([pop_music_seventies])
dolly_parton = Module("DollyParton")
dolly_parton.requires_modules.extend([country_pop])
taylor_swift = Module("TaylorSwift")
taylor_swift.requires_modules.extend([country_pop])
euro_pop = Module("EuroPop")
euro_pop.requires_modules.extend([pop_music_seventies])
abba = Module("Abba")
abba.requires_modules.extend([euro_pop])
pop_music_eighties = Module("PopMusicEighties")
pop_music_eighties.requires_modules.extend(
    [bubblegom_pop, baroque_pop, country_pop, euro_pop]
)
synthesizer_in_the_eighties = Module("SynthesizerInTheEighties")
synthesizer_in_the_eighties.requires_modules.extend([pop_music_eighties])
dance_pop = Module("DancePop")
dance_pop.requires_modules.extend([pop_music_eighties])
michael_jackson = Module("MichaelJackson")
michael_jackson.requires_modules.extend([dance_pop])
madonna = Module("Madonna")
madonna.requires_modules.extend([dance_pop])
pop_music_nineties = Module("PopMusicNineties")
pop_music_nineties.requires_modules.extend([dance_pop, synthesizer_in_the_eighties])
boys_girls_bands = Module("BoysGirlsBands")
boys_girls_bands.requires_modules.extend([pop_music_nineties])
spice_girls = Module("SpiceGirls")
spice_girls.requires_modules.extend([boys_girls_bands])
britney_spears = Module("BritneySpears")
britney_spears.requires_modules.extend([pop_music_nineties])
pop_music_2000 = Module("PopMusic2000")
pop_music_2000.requires_modules.extend([boys_girls_bands, britney_spears])
brit_pop = Module("BritPop")
brit_pop.requires_modules.extend([pop_music_2000])
oasis = Module("Oasis")
oasis.requires_modules.extend([brit_pop])
pop_and_hip_hop = Module("PopAndHipHop")
pop_and_hip_hop.requires_modules.extend([pop_music_2000])
rihanna = Module("Rihanna")
rihanna.requires_modules.extend([pop_and_hip_hop])
lady_gaga = Module("LadyGaga")
lady_gaga.requires_modules.extend([pop_and_hip_hop])
pop_music_today = Module("PopMusicToday")
pop_music_today.requires_modules.extend([brit_pop, pop_and_hip_hop])
dua_lipa = Module("DuaLipa")
dua_lipa.requires_modules.extend([pop_music_today])
ariana_grande = Module("ArianaGrande")
ariana_grande.requires_modules.extend([pop_music_today])
k_pop = Module("KPop")
k_pop.requires_modules.extend([pop_music_today])
bts = Module("BTS")
bts.requires_modules.extend([k_pop])

# Pop music analysis
pop_music_structure = Module("PopMusicStructure")
pop_music_structure.requires_modules.extend([bts, ariana_grande, dua_lipa])
pop_music_song_themes = Module("PopMusicSongThemes")
pop_music_song_themes.requires_modules.extend([pop_music_structure])
pop_music_rhythms = Module("PopMusicRhythms")
pop_music_rhythms.requires_modules.extend([pop_music_structure])
pop_music_harmonics = Module("PopMusicChords")
pop_music_harmonics.requires_modules.extend([pop_music_structure])
pop_music_band_structure = Module("PopMusicBandStructure")
pop_music_band_structure.requires_modules.extend([pop_music_structure])
pop_music_singing = Module("PopMusicSinging")
pop_music_singing.requires_modules.extend([pop_music_band_structure])
pop_music_accompaniment = Module("PopMusicAccompaniment")
pop_music_accompaniment.requires_modules.extend([pop_music_band_structure])
pop_music_bass = Module("PopMusicBass")
pop_music_bass.requires_modules.extend([pop_music_band_structure])
pop_music_percussions = Module("PopMusicPercussions")
pop_music_percussions.requires_modules.extend([pop_music_band_structure])
pop_music_effects = Module("PopMusicEffects")
pop_music_effects.requires_modules.extend([pop_music_band_structure])
pop_music_composition = Module("PopMusicComposition")
pop_music_composition.requires_modules.extend(
    [
        pop_music_song_themes,
        pop_music_rhythms,
        pop_music_harmonics,
        pop_music_singing,
        pop_music_accompaniment,
        pop_music_bass,
        pop_music_percussions,
        pop_music_effects,
    ]
)
pop_music_dance = Module("PopMusicDance")
pop_music_dance.requires_modules.extend([pop_music_composition])
pop_music_video_clip = Module("PopMusicVideoClip")
pop_music_video_clip.requires_modules.extend([pop_music_dance])

# Environment of pop music
pop_music_production = Module("PopMusicProduction")
pop_music_production.requires_modules.extend([pop_music_video_clip])
pop_music_and_the_body = Module("PopMusicAndTheBody")
pop_music_and_the_body.requires_modules.extend([pop_music_video_clip])
pop_music_cult_of_personality = Module("PopMusicCultOfPersonality")
pop_music_cult_of_personality.requires_modules.extend(
    [pop_music_and_the_body, pop_music_production]
)
pop_music_and_the_press = Module("PopMusicAndThePress")
pop_music_and_the_press.requires_modules.extend([pop_music_cult_of_personality])
pop_music_on_social_media = Module("PopMusicOnSocialMedia")
pop_music_on_social_media.requires_modules.extend([pop_music_and_the_press])
pop_music_shows = Module("PopMusicShows")
pop_music_shows.requires_modules.extend([pop_music_and_the_press])
pop_music_bands_and_their_fans = Module("PopMusicBandsAndTheirFans")
pop_music_bands_and_their_fans.requires_modules.extend(
    [pop_music_on_social_media, pop_music_shows]
)


pop_music_modules = [
    pop_music_presentation,
    pop_music_famous_artists,
    pop_music_festivals,
    difficulty_to_study_musical_style,
    pop_music_origin,
    rock_n_roll_presentation,
    rock_presentation,
    pop_music_sixties,
    beatles,
    pop_music_seventies,
    bubblegom_pop,
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
    oasis,
    pop_and_hip_hop,
    rihanna,
    lady_gaga,
    pop_music_today,
    dua_lipa,
    ariana_grande,
    k_pop,
    bts,
    pop_music_structure,
    pop_music_song_themes,
    pop_music_rhythms,
    pop_music_harmonics,
    pop_music_band_structure,
    pop_music_singing,
    pop_music_accompaniment,
    pop_music_bass,
    pop_music_percussions,
    pop_music_effects,
    pop_music_composition,
    pop_music_dance,
    pop_music_video_clip,
    pop_music_production,
    pop_music_and_the_body,
    pop_music_cult_of_personality,
    pop_music_and_the_press,
    pop_music_on_social_media,
    pop_music_shows,
    pop_music_bands_and_their_fans,
]

# Relations

pop_music.has_a_module.extend(pop_music_modules)

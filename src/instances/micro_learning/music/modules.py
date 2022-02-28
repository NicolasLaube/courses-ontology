"""Biology modules"""
from src.builder import ONTOLOGY
from src.construction.micro_learning.micro_learning_classes import Module
from src.instances.micro_learning.music.courses import pop_music, rock_music

with ONTOLOGY:
    # Pop music course

    # Introduction part
    pop_music_presentation = Module("PopMusicPresentation")
    pop_music_famous_artists = Module("PopMusicFamousArtists")
    pop_music_famous_artists.requires_module.extend([pop_music_presentation])
    pop_music_festivals = Module("PopMusicFestivals")
    pop_music_festivals.requires_module.extend([pop_music_famous_artists])
    difficulty_to_study_musical_style = Module("DifficultyToStudyMusicalStyle")
    difficulty_to_study_musical_style.requires_module.extend([pop_music_presentation])

    # History of pop music
    pop_music_origin = Module("PopMusicOrigin")
    pop_music_origin.requires_module.extend([pop_music_festivals])
    rock_n_roll_presentation = Module("RockNRollPresentation")
    rock_n_roll_presentation.requires_module.extend([pop_music_origin])
    rock_music_summary = Module("RockMusicSummary")
    rock_music_summary.requires_module.extend([rock_n_roll_presentation])
    pop_music_sixties = Module("PopMusicSixties")
    pop_music_sixties.requires_module.extend([rock_n_roll_presentation])
    beatles = Module("Beatles")
    beatles.requires_module.extend([pop_music_sixties])
    pop_music_seventies = Module("PopMusicSeventies")
    pop_music_seventies.requires_module.extend([pop_music_sixties])
    bubblegum_pop = Module("BubblegumPop")
    bubblegum_pop.requires_module.extend([pop_music_seventies])
    baroque_pop = Module("BaroquePop")
    baroque_pop.requires_module.extend([pop_music_seventies])
    beach_boys = Module("BeachBoys")
    beach_boys.requires_module.extend([baroque_pop])
    country_pop = Module("CountryPop")
    country_pop.requires_module.extend([pop_music_seventies])
    dolly_parton = Module("DollyParton")
    dolly_parton.requires_module.extend([country_pop])
    taylor_swift = Module("TaylorSwift")
    taylor_swift.requires_module.extend([country_pop])
    euro_pop = Module("EuroPop")
    euro_pop.requires_module.extend([pop_music_seventies])
    abba = Module("Abba")
    abba.requires_module.extend([euro_pop])
    pop_music_eighties = Module("PopMusicEighties")
    pop_music_eighties.requires_module.extend(
        [bubblegum_pop, baroque_pop, country_pop, euro_pop]
    )
    synthesizer_in_the_eighties = Module("SynthesizerInTheEighties")
    synthesizer_in_the_eighties.requires_module.extend([pop_music_eighties])
    dance_pop = Module("DancePop")
    dance_pop.requires_module.extend([pop_music_eighties])
    michael_jackson = Module("MichaelJackson")
    michael_jackson.requires_module.extend([dance_pop])
    madonna = Module("Madonna")
    madonna.requires_module.extend([dance_pop])
    pop_music_nineties = Module("PopMusicNineties")
    pop_music_nineties.requires_module.extend([dance_pop, synthesizer_in_the_eighties])
    boys_girls_bands = Module("BoysGirlsBands")
    boys_girls_bands.requires_module.extend([pop_music_nineties])
    spice_girls = Module("SpiceGirls")
    spice_girls.requires_module.extend([boys_girls_bands])
    britney_spears = Module("BritneySpears")
    britney_spears.requires_module.extend([pop_music_nineties])
    pop_music_2000 = Module("PopMusic2000")
    pop_music_2000.requires_module.extend([boys_girls_bands, britney_spears])
    brit_pop = Module("BritPop")
    brit_pop.requires_module.extend([pop_music_2000])
    oasis = Module("Oasis")
    oasis.requires_module.extend([brit_pop])
    pop_and_hip_hop = Module("PopAndHipHop")
    pop_and_hip_hop.requires_module.extend([pop_music_2000])
    rihanna = Module("Rihanna")
    rihanna.requires_module.extend([pop_and_hip_hop])
    lady_gaga = Module("LadyGaga")
    lady_gaga.requires_module.extend([pop_and_hip_hop])
    pop_music_today = Module("PopMusicToday")
    pop_music_today.requires_module.extend([brit_pop, pop_and_hip_hop])
    dua_lipa = Module("DuaLipa")
    dua_lipa.requires_module.extend([pop_music_today])
    ariana_grande = Module("ArianaGrande")
    ariana_grande.requires_module.extend([pop_music_today])
    k_pop = Module("KPop")
    k_pop.requires_module.extend([pop_music_today])
    bts = Module("BTS")
    bts.requires_module.extend([k_pop])

    # Pop music analysis
    pop_music_structure = Module("PopMusicStructure")
    pop_music_structure.requires_module.extend([bts, ariana_grande, dua_lipa])
    pop_music_song_themes = Module("PopMusicSongThemes")
    pop_music_song_themes.requires_module.extend([pop_music_structure])
    pop_music_rhythms = Module("PopMusicRhythms")
    pop_music_rhythms.requires_module.extend([pop_music_structure])
    pop_music_harmonics = Module("PopMusicChords")
    pop_music_harmonics.requires_module.extend([pop_music_structure])
    pop_music_band_structure = Module("PopMusicBandStructure")
    pop_music_band_structure.requires_module.extend([pop_music_structure])
    pop_music_singing = Module("PopMusicSinging")
    pop_music_singing.requires_module.extend([pop_music_band_structure])
    pop_music_accompaniment = Module("PopMusicAccompaniment")
    pop_music_accompaniment.requires_module.extend([pop_music_band_structure])
    pop_music_bass = Module("PopMusicBass")
    pop_music_bass.requires_module.extend([pop_music_band_structure])
    pop_music_percussions = Module("PopMusicPercussions")
    pop_music_percussions.requires_module.extend([pop_music_band_structure])
    pop_music_effects = Module("PopMusicEffects")
    pop_music_effects.requires_module.extend([pop_music_band_structure])
    pop_music_composition = Module("PopMusicComposition")
    pop_music_composition.requires_module.extend(
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
    pop_music_dance.requires_module.extend([pop_music_composition])
    pop_music_video_clip = Module("PopMusicVideoClip")
    pop_music_video_clip.requires_module.extend([pop_music_dance])

    # Environment of pop music
    pop_music_production = Module("PopMusicProduction")
    pop_music_production.requires_module.extend([pop_music_video_clip])
    pop_music_and_the_body = Module("PopMusicAndTheBody")
    pop_music_and_the_body.requires_module.extend([pop_music_video_clip])
    pop_music_cult_of_personality = Module("PopMusicCultOfPersonality")
    pop_music_cult_of_personality.requires_module.extend(
        [pop_music_and_the_body, pop_music_production]
    )
    pop_music_and_the_press = Module("PopMusicAndThePress")
    pop_music_and_the_press.requires_module.extend([pop_music_cult_of_personality])
    pop_music_on_social_media = Module("PopMusicOnSocialMedia")
    pop_music_on_social_media.requires_module.extend([pop_music_and_the_press])
    pop_music_shows = Module("PopMusicShows")
    pop_music_shows.requires_module.extend([pop_music_and_the_press])
    pop_music_bands_and_their_fans = Module("PopMusicBandsAndTheirFans")
    pop_music_bands_and_their_fans.requires_module.extend(
        [pop_music_on_social_media, pop_music_shows]
    )

    pop_music_modules = [
        pop_music_presentation,
        pop_music_famous_artists,
        pop_music_festivals,
        difficulty_to_study_musical_style,
        pop_music_origin,
        rock_n_roll_presentation,
        rock_music_summary,
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

    pop_music.has_as_module.extend(pop_music_modules)

    # Rock music course

    # Introduction part
    rock_music_presentation = Module("RockMusicPresentation")
    rock_music_famous_artists = Module("RockMusicFamousArtists")
    rock_music_famous_artists.requires_module.extend([rock_music_presentation])
    rock_music_festivals = Module("RockMusicFestivals")
    rock_music_festivals.requires_module.extend([rock_music_famous_artists])
    # difficulty_to_study_musical_style already defined
    difficulty_to_study_musical_style.requires_module.extend([rock_music_presentation])

    # History of rock music
    rock_music_origin = Module("RockMusicOrigin")
    rock_music_origin.requires_module.extend([rock_music_festivals])
    # rock_n_roll_presentation already defined
    rock_n_roll_presentation.requires_module.extend([rock_music_origin])
    rockabily = Module("Rockabily")
    rockabily.requires_module.extend([rock_n_roll_presentation])
    elvis_presley = Module("ElvisPresley")
    elvis_presley.requires_module.extend([rockabily])
    chuck_berry = Module("ChuckBerry")
    chuck_berry.requires_module.extend([rockabily])
    doo_wop = Module("DooWop")
    doo_wop.requires_module.extend([rock_n_roll_presentation])
    pop_music_summary = Module("PopMusicSummary")
    pop_music_summary.requires_module.extend([rockabily, doo_wop])
    rock_music_sixties = Module("RockMusicSixties")
    rock_music_sixties.requires_module.extend([pop_music_summary])
    rolling_stones = Module("RollingStones")
    rolling_stones.requires_module.extend([rock_music_sixties])
    mod_subculture = Module("ModSubculture")
    mod_subculture.requires_module.extend([rolling_stones])
    the_who = Module("TheWho")
    the_who.requires_module.extend([mod_subculture])
    blues_rock = Module("BluesRock")
    blues_rock.requires_module.extend([rolling_stones])
    the_animals = Module("TheAnimals")
    the_animals.requires_module.extend([blues_rock])
    folk_music = Module("FolkMusic")
    folk_music.requires_module.extend([mod_subculture, blues_rock])
    bob_dylan = Module("BobDylan")
    bob_dylan.requires_module.extend([folk_music])
    psychedelia = Module("Psychedelia")
    psychedelia.requires_module.extend([mod_subculture, blues_rock])
    pink_floyd = Module("PinkFloyd")
    pink_floyd.requires_module.extend([psychedelia])
    the_doors = Module("TheDoors")
    the_doors.requires_module.extend([psychedelia])
    progressive_rock = Module("ProgressiveRock")
    progressive_rock.requires_module.extend([psychedelia])
    king_crimson = Module("KingCrimson")
    king_crimson.requires_module.extend([progressive_rock])
    genesis = Module("Genesis")
    genesis.requires_module.extend([progressive_rock])
    jimi_hendrix = Module("JimiHendrix")
    jimi_hendrix.requires_module.extend([progressive_rock])
    garage_rock = Module("GarageRock")
    garage_rock.requires_module.extend([mod_subculture, blues_rock])
    jazz_fusion = Module("JazzFusion")
    jazz_fusion.requires_module.extend([mod_subculture, blues_rock])
    rock_music_seventies = Module("RockMusicSeventies")
    rock_music_seventies.requires_module.extend(
        [jazz_fusion, garage_rock, progressive_rock, folk_music]
    )
    soft_rock = Module("SoftRock")
    soft_rock.requires_module.extend([rock_music_seventies])
    elton_john = Module("EltonJohn")
    elton_john.requires_module.extend([soft_rock])
    hard_rock = Module("HardRock")
    hard_rock.requires_module.extend([rock_music_seventies])
    led_zeppelin = Module("LedZeppelin")
    led_zeppelin.requires_module.extend([hard_rock])
    deep_purple = Module("DeepPurple")
    deep_purple.requires_module.extend([hard_rock])
    black_sabbath = Module("BlackSabbath")
    black_sabbath.requires_module.extend([hard_rock])
    acdc = Module("ACDC")
    acdc.requires_module.extend([hard_rock])
    glam_rock = Module("GlamRock")
    glam_rock.requires_module.extend([rock_music_seventies])
    david_bowie = Module("DavidBowie")
    david_bowie.requires_module.extend([glam_rock])
    queen = Module("Queen")
    queen.requires_module.extend([glam_rock])
    punk_rock = Module("PunkRock")
    punk_rock.requires_module.extend([rock_music_seventies])
    sex_pistols = Module("SexPistols")
    sex_pistols.requires_module.extend([punk_rock])
    rock_music_eighties = Module("RockMusicEighties")
    rock_music_eighties.requires_module.extend(
        [soft_rock, hard_rock, glam_rock, punk_rock]
    )
    heavy_metal = Module("HeavyMetal")
    heavy_metal.requires_module.extend([rock_music_eighties])
    iron_maiden = Module("IronMaiden")
    iron_maiden.requires_module.extend([heavy_metal])
    motorhead = Module("Motorhead")
    motorhead.requires_module.extend([heavy_metal])
    metallica = Module("Metallica")
    metallica.requires_module.extend([heavy_metal])
    indie_rock = Module("IndieRock")
    indie_rock.requires_module.extend([rock_music_eighties])
    pixies = Module("Pixies")
    pixies.requires_module.extend([indie_rock])
    glam_metal = Module("GlamMetal")
    glam_metal.requires_module.extend([heavy_metal])
    kiss = Module("Kiss")
    kiss.requires_module.extend([glam_metal])
    new_wave_music = Module("NewWaveMusic")
    new_wave_music.requires_module.extend([rock_music_eighties])
    the_cure = Module("TheCure")
    the_cure.requires_module.extend([new_wave_music])
    the_police = Module("ThePolice")
    the_police.requires_module.extend([new_wave_music])
    rock_music_nineties = Module("RockMusicNineties")
    rock_music_nineties.requires_module.extend([glam_metal, indie_rock, new_wave_music])
    alternative_rock = Module("AlternativeRock")
    alternative_rock.requires_module.extend([rock_music_nineties])
    red_hot_chili_peppers = Module("RedHotChiliPeppers")
    red_hot_chili_peppers.requires_module.extend([alternative_rock])
    muse = Module("Muse")
    muse.requires_module.extend([alternative_rock])
    radiohead = Module("Radiohead")
    radiohead.requires_module.extend([alternative_rock])
    # brit_pop already defined
    brit_pop.requires_module.extend([alternative_rock])
    # oasis already defined
    # oasis.requires_module.extend([brit_pop])
    grunge = Module("Grunge")
    grunge.requires_module.extend([alternative_rock])
    nirvana = Module("Nirvana")
    nirvana.requires_module.extend([grunge])
    rock_fusion_90s = Module("RockFusion90s")
    rock_fusion_90s.requires_module.extend([rock_music_nineties])
    rage_against_the_machine = Module("RageAgainstTheMachine")
    rage_against_the_machine.requires_module.extend([rock_fusion_90s])
    system_of_a_down = Module("SystemOfADown")
    system_of_a_down.requires_module.extend([rock_fusion_90s])
    rock_music_2000 = Module("RockMusic2000")
    rock_music_2000.requires_module.extend(
        [alternative_rock, brit_pop, grunge, rock_fusion_90s]
    )
    neo_garage_rock = Module("NeoGarageRock")
    neo_garage_rock.requires_module.extend([rock_music_2000])
    arctic_monkeys = Module("ArcticMonkeys")
    arctic_monkeys.requires_module.extend([neo_garage_rock])
    emocore = Module("Emocore")
    emocore.requires_module.extend([rock_music_2000])
    dance_punk = Module("DancePunk")
    dance_punk.requires_module.extend([rock_music_2000])
    contemporary_rock = Module("ContemporaryRock")
    contemporary_rock.requires_module.extend([neo_garage_rock, emocore, dance_punk])

    # Rock music analysis
    rock_music_structure = Module("RockMusicStructure")
    rock_music_structure.requires_module.extend([contemporary_rock])
    rock_music_song_themes = Module("RockMusicSongThemes")
    rock_music_song_themes.requires_module.extend([rock_music_structure])
    rock_music_rhythms = Module("RockMusicRhythms")
    rock_music_rhythms.requires_module.extend([rock_music_structure])
    rock_music_harmonics = Module("RockMusicChords")
    rock_music_harmonics.requires_module.extend([rock_music_structure])
    rock_music_band_structure = Module("RockMusicBandStructure")
    rock_music_band_structure.requires_module.extend([rock_music_structure])
    rock_music_singing = Module("RockMusicSinging")
    rock_music_singing.requires_module.extend([rock_music_band_structure])
    rock_music_accompaniment = Module("RockMusicAccompaniment")
    rock_music_accompaniment.requires_module.extend([rock_music_band_structure])
    rock_music_bass = Module("RockMusicBass")
    rock_music_bass.requires_module.extend([rock_music_band_structure])
    rock_music_percussions = Module("RockMusicPercussions")
    rock_music_percussions.requires_module.extend([rock_music_band_structure])
    rock_music_effects = Module("RockMusicEffects")
    rock_music_effects.requires_module.extend([rock_music_band_structure])
    rock_music_composition = Module("RockMusicComposition")
    rock_music_composition.requires_module.extend(
        [
            rock_music_song_themes,
            rock_music_rhythms,
            rock_music_harmonics,
            rock_music_singing,
            rock_music_accompaniment,
            rock_music_bass,
            rock_music_percussions,
            rock_music_effects,
        ]
    )
    rock_music_recording = Module("RockMusicRecording")
    rock_music_recording.requires_module.extend([rock_music_composition])

    # Environment of rock music
    rock_social_background = Module("RockSocialBackground")
    rock_social_background.requires_module.extend([rock_music_recording])
    rock_spirit = Module("RockSpirit")
    rock_spirit.requires_module.extend([rock_social_background])
    counterculture_movement = Module("CountercultureMovement")
    counterculture_movement.requires_module.extend([rock_spirit])
    rock_music_production = Module("RockMusicProduction")
    rock_music_production.requires_module.extend([counterculture_movement])
    counterculture_in_the_sixties = Module("CounterCultureInTheSixties")
    counterculture_in_the_sixties.requires_module.extend([counterculture_movement])
    woodstock_festival = Module("WoodstockFestival")
    woodstock_festival.requires_module.extend([counterculture_in_the_sixties])
    rock_political_activism = Module("RockPoliticalActivism")
    rock_political_activism.requires_module.extend([counterculture_movement])
    live_aid = Module("LiveAid")
    live_aid.requires_module.extend([rock_political_activism])
    rock_music_and_the_press = Module("RockMusicAndThePress")
    rock_music_and_the_press.requires_module.extend(
        [rock_music_production, counterculture_in_the_sixties, rock_political_activism]
    )
    rock_music_shows = Module("RockMusicShows")
    rock_music_shows.requires_module.extend([rock_spirit])
    rock_music_and_sex = Module("RockMusicAndSex")
    rock_music_and_sex.requires_module.extend([rock_music_shows])
    rock_music_and_drugs = Module("RockMusicAndDrugs")
    rock_music_and_drugs.requires_module.extend([rock_music_shows])
    rock_music_bands_and_their_fans = Module("RockMusicBandsAndTheirFans")
    rock_music_bands_and_their_fans.requires_module.extend([rock_music_shows])
    fanzines = Module("Fanzines")
    fanzines.requires_module.extend([rock_music_bands_and_their_fans])
    women_in_rock_music = Module("WomenInRockMusic")
    women_in_rock_music.requires_module.extend([rock_spirit])

    rock_music_modules = [
        rock_music_presentation,
        rock_music_famous_artists,
        rock_music_festivals,
        difficulty_to_study_musical_style,
        rock_music_origin,
        rock_n_roll_presentation,
        rockabily,
        elvis_presley,
        chuck_berry,
        doo_wop,
        pop_music_summary,
        rock_music_sixties,
        rolling_stones,
        mod_subculture,
        the_who,
        blues_rock,
        the_animals,
        folk_music,
        bob_dylan,
        psychedelia,
        pink_floyd,
        the_doors,
        progressive_rock,
        king_crimson,
        genesis,
        jimi_hendrix,
        garage_rock,
        jazz_fusion,
        rock_music_seventies,
        soft_rock,
        elton_john,
        hard_rock,
        led_zeppelin,
        deep_purple,
        black_sabbath,
        acdc,
        glam_rock,
        david_bowie,
        queen,
        punk_rock,
        sex_pistols,
        rock_music_eighties,
        heavy_metal,
        iron_maiden,
        motorhead,
        metallica,
        indie_rock,
        pixies,
        glam_metal,
        kiss,
        new_wave_music,
        the_cure,
        the_police,
        rock_music_nineties,
        alternative_rock,
        red_hot_chili_peppers,
        muse,
        radiohead,
        brit_pop,
        oasis,
        grunge,
        nirvana,
        rock_fusion_90s,
        rage_against_the_machine,
        system_of_a_down,
        rock_music_2000,
        neo_garage_rock,
        arctic_monkeys,
        emocore,
        dance_punk,
        contemporary_rock,
        rock_music_structure,
        rock_music_song_themes,
        rock_music_rhythms,
        rock_music_harmonics,
        rock_music_band_structure,
        rock_music_singing,
        rock_music_accompaniment,
        rock_music_bass,
        rock_music_percussions,
        rock_music_effects,
        rock_music_composition,
        rock_music_recording,
        rock_social_background,
        rock_spirit,
        counterculture_movement,
        rock_music_production,
        counterculture_in_the_sixties,
        woodstock_festival,
        rock_political_activism,
        live_aid,
        rock_music_and_the_press,
        rock_music_shows,
        rock_music_and_sex,
        rock_music_and_drugs,
        rock_music_bands_and_their_fans,
        fanzines,
        women_in_rock_music,
    ]

    # Relations

    rock_music.has_as_module.extend(rock_music_modules)

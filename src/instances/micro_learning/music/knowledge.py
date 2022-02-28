"""Biology modules"""
from src.builder import ONTOLOGY
from src.construction.micro_learning.micro_learning_classes import Knowledge
from src.instances.micro_learning.music.modules import (
    baroque_pop,
    beach_boys,
    beatles,
    bubblegum_pop,
    country_pop,
    dolly_parton,
    pop_music_2000,
    pop_music_eighties,
    pop_music_nineties,
    pop_music_origin,
    pop_music_seventies,
    rock_n_roll_presentation,
    taylor_swift,
)

with ONTOLOGY:
    # Pop music course

    first_apparition_of_pop_term = Knowledge("FirstApparitionOfPopTerm")
    origin_country_of_pop_term = Knowledge("OriginCountryOfPopTerm")
    term_development_among_young = Knowledge("TermDevelopmentAmongYoung")
    in_50s_pop_doesnt_design_a_musical_style = Knowledge(
        "Int50sPopDoesntDesignAMusicalStyle"
    )
    # add to module
    pop_music_origin.has_as_knowledge.extend(
        [
            first_apparition_of_pop_term,
            origin_country_of_pop_term,
            term_development_among_young,
            in_50s_pop_doesnt_design_a_musical_style,
        ]
    )

    in_50s_rocknroll_dominates = Knowledge("In50sRocknRollDominates")
    elvis_presly_famous_rocknroll_artist = Knowledge(
        "ElvisPresleyFamousRocknRollArtist"
    )
    jailhouse_music_from_elvis = Knowledge("JailhouseRockIsFromElvisPresley")
    jailhouse_music_publication = Knowledge("JailhouseRockPublishedIn1958")
    rocknroll_subdivision = Knowledge("InThe1950sRocknRollSubdivision")
    rocknroll_2_subdivision_branches = Knowledge("RocknRollSubdivisionBranches")
    blues_not_in_subdivision = Knowledge("BluesNotInSubdivision")
    rock_faithful_to_the_blues = Knowledge("RockFaithfulToTheBlues")

    # add to module
    rock_n_roll_presentation.has_as_knowledge.extend(
        [
            in_50s_rocknroll_dominates,
            elvis_presly_famous_rocknroll_artist,
            jailhouse_music_from_elvis,
            jailhouse_music_publication,
            rocknroll_subdivision,
            rocknroll_2_subdivision_branches,
            blues_not_in_subdivision,
            rock_faithful_to_the_blues,
        ]
    )

    # creation of pop
    first_pop_music = Knowledge("YesterdayIsConsideredFirstPopMusic")
    yesterday_publication = Knowledge("YesterdayPublishedIn1965InTheUK")
    first_pop_music_group = Knowledge("BeatlesFirstPopMusicGroup")
    beatles_english_group = Knowledge("BeatlesIsAEnglishGroup")
    beatles_formed_in_liverpool = Knowledge("BeatlesFormedInLiverpool")
    beatles_one_of_most_popular = Knowledge("BeatlesOneOfMostPopular")
    beatles_members = Knowledge(
        "MembersAreJohnLennonPaulMcCartneyGeorgeHarrisonRingoStarr"
    )
    beatles_founder = Knowledge("JohnLennonFounder")
    beatles_creation_in_1957 = Knowledge("BeatlesCreatedIn1957")
    beatles_last_member = Knowledge("RingoStarrLastMember")

    # add to module
    beatles.has_as_knowledge.extend(
        [
            first_pop_music,
            yesterday_publication,
            first_pop_music_group,
            beatles_english_group,
            beatles_formed_in_liverpool,
            beatles_one_of_most_popular,
            beatles_members,
            beatles_founder,
            beatles_creation_in_1957,
            beatles_last_member,
        ]
    )

    # caracteristics of pop
    pop_turned_towards_lighter_themes = Knowledge("PopTurnedToLighterThematics")
    pop_musics_structures_are_simple = Knowledge("PopMusicStructuresAreSimple")
    pop_music_melodies_stay_in_mind = Knowledge("PopMusicMelodiesStayInMind")
    pop_music_short = Knowledge("PopMusicsAreShort")
    pop_music_highlights_musicians = Knowledge("PopMusicHighlightsMusicians")

    # add to module
    pop_music_seventies.has_as_knowledge.extend(
        [
            pop_turned_towards_lighter_themes,
            pop_musics_structures_are_simple,
            pop_music_melodies_stay_in_mind,
            pop_music_short,
            pop_music_highlights_musicians,
        ]
    )

    # bubblegum pop
    bubblegum_pop_is_subgenre_of_pop = Knowledge("BubbleGumPopIsSubgenreOfPop")
    bubblegum_pop_created_for_teenagers = Knowledge("BubblegumPopCreatedForTeenagers")
    bubblegum_pop_exploited_by_brands = Knowledge("BubblegumPopExploitedBysBrands")
    archies_sugar_is_bubblegum_pop = Knowledge("ArchiesSugarIsBubblegumPop")
    bubblegum_pop_because_of_teens_bubblegum = Knowledge(
        "BubblegumPopBecauseOfTeensBubblegum"
    )

    bubblegum_pop.has_as_knowledge.extend(
        [
            bubblegum_pop_is_subgenre_of_pop,
            bubblegum_pop_created_for_teenagers,
            bubblegum_pop_exploited_by_brands,
            archies_sugar_is_bubblegum_pop,
            bubblegum_pop_because_of_teens_bubblegum,
        ]
    )

    # baroque pop
    pop_baroque_is_subgenre_of_pop = Knowledge("PopBaroqueIsSubgenreOfPop")
    pop_baroque_mixes_classical_baroque_and_pop = Knowledge(
        "PopBaroqueMixesClassicalBaroqueAndPop"
    )
    pop_baroque_uses_instruments_of_classical_musique = Knowledge(
        "PopBaroqueUsesInstrumentsOfClassicalMusique"
    )
    wouldnt_it_be_nice_is_pop_baroque = Knowledge("WouldntItBeNiceIsPopBaroque")
    wouldnt_it_be_nice_contains_piano = Knowledge("WouldntItBeNiceContainsPiano")
    wouldnt_it_be_nice_from_beach_boys = Knowledge("WouldntItBeNiceFromBeachBoys")

    baroque_pop.has_as_knowledge.extend(
        [
            pop_baroque_is_subgenre_of_pop,
            pop_baroque_mixes_classical_baroque_and_pop,
            pop_baroque_uses_instruments_of_classical_musique,
        ]
    )

    beach_boys.has_as_knowledge.extend(
        [
            wouldnt_it_be_nice_is_pop_baroque,
            wouldnt_it_be_nice_contains_piano,
            wouldnt_it_be_nice_from_beach_boys,
        ]
    )

    # country pop
    country_pop_is_subgenre_of_pop = Knowledge("CountryPopIsSubgenreOfPop")
    country_pop_developed_by_members_of_country_musique_for_audience = Knowledge(
        "PopCountryDevelopedForLargerAudienceByCountryMusicians"
    )
    iconic_instrument_of_country_is_harmonica = Knowledge(
        "IconicInstrumentOfCountryIsHarmonica"
    )

    country_pop.has_as_knowledge.extend(
        [
            country_pop_is_subgenre_of_pop,
            country_pop_developed_by_members_of_country_musique_for_audience,
            iconic_instrument_of_country_is_harmonica,
        ]
    )

    ill_always_love_you_is_pop_country = Knowledge("IllAlwaysLoveYouIsPopCountry")
    ill_always_love_you_from_dolly_parton = Knowledge("IllAlwaysLoveYouFromDollyParton")

    dolly_parton.has_as_knowledge.extend(
        [ill_always_love_you_is_pop_country, ill_always_love_you_from_dolly_parton]
    )

    contemporary_artist_of_pop_country_Taylor_S = Knowledge(
        "TaylorsSwiftContemporaryArtistOfPopCountry"
    )

    taylor_swift.has_as_knowledge.extend([contemporary_artist_of_pop_country_Taylor_S])
    # 80s
    synthetizer_appeared_in_80s = Knowledge("SynthetizerAppearedInThe80s")
    synthetizer_had_important_impact_on_all_music_styles = Knowledge(
        "SynthetizerHadImportantImpactOnAllMusicStyles"
    )
    dance_pop_is_subgenre_of_pop_music = Knowledge("DancePopIsSubgenreOfPop")
    dance_pop_appeared_with_synthetizers = Knowledge("DancePopAppearedWithSynthetizers")
    dance_pop_has_quick_tempo = Knowledge("DancePopHasQuickTempo")
    dance_pop_has_catchy_music = Knowledge("DancePopHasCatchyMusic")
    dance_pop_emphesizes_on_video_clips = Knowledge("DancePopEmphesizesOnVideoClips")
    michael_jackson_considered_king_of_pop = Knowledge(
        "MichaelJacksonConsideredKingOfPop"
    )
    micheal_jackson_artist_the_most_successful = Knowledge(
        "MichealJacksonArtistTheMostSuccessful"
    )
    billie_jean_is_from_micheal_jackson = Knowledge("BillieJeanIsFromMichealJackson")
    thriller_is_mj_s_most_sold_album = Knowledge("ThrillerIsMJsMostSoldAlbum")
    thriller_is_most_sold_album = Knowledge("ThrillerMostSoldAlbum")
    thriller_sold_66_million_exemplars = Knowledge("ThrillerSold66MExamplarsIn1982")
    madonna_queen_of_pop = Knowledge("MadonnaQueenOfPop")
    madonna_singer_who_most_sold_disks = Knowledge("MadonnaSoldMostDisks")
    madonna_was_dancer_before = Knowledge("MadonnaWasDanceBefore")
    madonna_did_iconic_dances_in_clips = Knowledge("MadonnaDidIconicDancesInClips")
    choregraphy_important_for_dance_pop = Knowledge("ChoregraphyImportantForDancePop")
    dance_pop_is_still_very_popular = Knowledge("DancePopIsStillVeryPopular")

    pop_music_eighties.has_as_knowledge.extend(
        [
            synthetizer_appeared_in_80s,
            synthetizer_had_important_impact_on_all_music_styles,
            dance_pop_is_subgenre_of_pop_music,
            dance_pop_appeared_with_synthetizers,
            dance_pop_has_quick_tempo,
            dance_pop_has_catchy_music,
            dance_pop_emphesizes_on_video_clips,
            michael_jackson_considered_king_of_pop,
            micheal_jackson_artist_the_most_successful,
            billie_jean_is_from_micheal_jackson,
            thriller_is_mj_s_most_sold_album,
            thriller_is_most_sold_album,
            thriller_sold_66_million_exemplars,
            madonna_queen_of_pop,
            madonna_singer_who_most_sold_disks,
            madonna_was_dancer_before,
            madonna_did_iconic_dances_in_clips,
            choregraphy_important_for_dance_pop,
            dance_pop_is_still_very_popular,
        ]
    )

    # 90s
    boys_girls_band_are_trendy_in90s = Knowledge("BoysBandsAreTrendyInThe90s")
    boys_girls_bands_group_handsome_boys_and_girls = Knowledge(
        "BoysBandsGroupHandsomeBoysAndGirls"
    )
    most_famous_girls_band_is_spice_grils = Knowledge("MostFamousGrilsBandSpiceGirl")
    most_famous_music_of_spice_grils_is_wannabe = Knowledge(
        "MostFamousMusicOfSpiceGirlsIsWannabe"
    )
    wannabe_ranked_top_in37_countries = Knowledge("WannabeRankedTopIn37Countries")
    wannabe_sold_more_than_7_m_copies = Knowledge("WannabeSoldMoreThan7MCopies")
    bg_groups_were_formed_by_producers_for_commercial_purposes = Knowledge(
        "BGGroupsWereFormedByProducersForCommercialPurposes"
    )

    britney_spears_is_considered_princess_of_pop = Knowledge(
        "BritneySpearsIsConsideredPrincessOfPop"
    )
    britney_spears_sold_most_disks_in_the_2000 = Knowledge(
        "BritneySpearsSoldMostDisksInThe2000"
    )
    britney_spears_sold_200_millions_disks_in_2000 = Knowledge(
        "BritneySpearsSoldMoreThan200MDisksIn2000"
    )
    babe_one_more_time_is_from_bs = Knowledge("BabeOneMoreTimeIsFromBS")

    pop_music_nineties.has_as_knowledge.extend(
        [
            boys_girls_band_are_trendy_in90s,
            boys_girls_bands_group_handsome_boys_and_girls,
            most_famous_girls_band_is_spice_grils,
            most_famous_music_of_spice_grils_is_wannabe,
            wannabe_ranked_top_in37_countries,
            wannabe_sold_more_than_7_m_copies,
            bg_groups_were_formed_by_producers_for_commercial_purposes,
            britney_spears_is_considered_princess_of_pop,
            britney_spears_sold_most_disks_in_the_2000,
            britney_spears_sold_200_millions_disks_in_2000,
            babe_one_more_time_is_from_bs,
        ]
    )

    # 2000s
    in_2000_pop_music_diversifies_again = Knowledge("In2000MusicPopDiversisifesAgain")
    brit_pop_subgenre_of_pop = Knowledge("BritPopSubgenreOfPop")
    brit_pop_comes_closer_to_rock_again = Knowledge("BritPopComesCloserToRockAgain")
    brit_pop_was_born_in_england = Knowledge("BritPopWasBornInEngland")
    brit_pop_is_inspired_by_60s_rock = Knowledge("BritPopIsInspiredBy60sRock")
    oasis_is_a_brit_pop_group = Knowledge("OasisIsABritPopGroup")

    rihanna_gets_closer_to_rnb = Knowledge("RihannaGetsCloserToRnb")
    jay_z_gets_closer_to_hip_hop = Knowledge("JayZGetsCloserToHipHop")
    hip_hop_contains_rapped_parts = Knowledge("HipHopContainsRappedParts")

    lady_gagas_music_is_more_electronic = Knowledge("LadyGagasMusicIsMoreElectronic")
    lady_gagas_music_is_new_wave = Knowledge("LadyGagasMusicIsNewWave")
    lady_gagas_has_smoothed_sound_environment = Knowledge(
        "LadyGagasMusicHasSmoothedSoundEnvironment"
    )

    pop_music_2000.has_as_knowledge.extend(
        [
            in_2000_pop_music_diversifies_again,
            brit_pop_subgenre_of_pop,
            brit_pop_comes_closer_to_rock_again,
            brit_pop_was_born_in_england,
            brit_pop_is_inspired_by_60s_rock,
            oasis_is_a_brit_pop_group,
            rihanna_gets_closer_to_rnb,
            jay_z_gets_closer_to_hip_hop,
            hip_hop_contains_rapped_parts,
            lady_gagas_music_is_more_electronic,
            lady_gagas_music_is_new_wave,
            lady_gagas_has_smoothed_sound_environment,
        ]
    )

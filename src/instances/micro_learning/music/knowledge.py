"""Biology modules"""
from src.builder import ONTOLOGY
from src.construction import Knowledge

with ONTOLOGY:
    # Pop music course

    first_apparition_of_pop_term = Knowledge("FirstApparitionOfPopTerm")
    origin_country_of_pop_term = Knowledge("OriginCountryOfPopTerm")
    term_development_among_young = Knowledge("TermDevelopmentAmongYoung")
    in_50s_pop_doesnt_design_a_musical_stryle = Knowledge(
        "Int50sPopDoesntDesignAMusicalStyle"
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
    # caracteristics of pop
    pop_turned_towards_lighter_themes = Knowledge("PopTurnedToLighterThematics")
    pop_musics_structures_are_simple = Knowledge("PopMusicStructuresAreSimple")
    pop_music_melodies_stay_in_mind = Knowledge("PopMusicMelodiesStayInMind")
    pop_music_short = Knowledge("PopMusicsAreShort")
    pop_music_highlights_musicians = Knowledge("PopMusicHighlightsMusicians")
    # bubblegum pop
    bubblegum_pop_is_subgenre_of_pop = Knowledge("BubbleGumPopIsSubgenreOfPop")
    bubblegum_pop_created_for_teenagers = Knowledge("BubblegumPopCreatedForTeenagers")
    bubblegum_pop_exploited_by_brands = Knowledge("BubblegumPopExploitedBysBrands")
    archies_sugar_is_bubblegum_pop = Knowledge("ArchiesSugarIsBubblegumPop")
    bubblegum_pop_because_of_teens_bubblegum = Knowledge(
        "BubblegumPopBecauseOfTeensBubblegum"
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
    # country pop
    country_pop_is_subgenre_of_pop = Knowledge("CountryPopIsSubgenreOfPop")
    country_pop_developed_by_members_of_country_musique_for_audience = Knowledge(
        "PopCountryDevelopedForLargerAudienceByCountryMusicians"
    )
    ill_always_love_you_is_pop_country = Knowledge("IllAlwaysLoveYouIsPopCountry")
    ill_always_love_you_from_dolly_parton = Knowledge("IllAlwaysLoveYouFromDollyParton")
    iconic_instrument_of_country_is_harmonica = Knowledge(
        "IconicInstrumentOfCountryIsHarmonica"
    )
    contemporary_artist_of_pop_country_Taylor_S = Knowledge(
        "TaylorsSwiftContemporaryArtistOfPopCountry"
    )

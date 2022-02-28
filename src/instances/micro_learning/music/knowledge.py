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
    pop_turned_towards_lighter_themes = Knowledge("2255211")

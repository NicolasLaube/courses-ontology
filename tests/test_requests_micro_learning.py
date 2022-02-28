"""Test Micro learning requests"""

import pytest

from src.builder import ONTOLOGY
from src.instances import pop_music_modules
from src.requests.requests_micro_learning import (
    get_all_courses,
    get_all_thematics,
    get_course_knowledge,
    get_course_modules,
    get_course_prerequisites,
    get_course_thematics,
    get_module_knowledge,
    get_module_prerequisites,
)

with ONTOLOGY:

    @pytest.mark.requests
    def test_courses_list() -> None:
        """Test course list"""
        true_courses_ = sorted(
            [
                ONTOLOGY.Microbiota.name,
                ONTOLOGY.TheoryOfEvolution.name,
                ONTOLOGY.NumericEconomy.name,
                ONTOLOGY.CurrencyAndFinancialInstituations.name,
                ONTOLOGY.PovertyAndInequalities.name,
                ONTOLOGY.Macroeconomy.name,
                ONTOLOGY.PopMusic.name,
                ONTOLOGY.ClassicalMusic.name,
                ONTOLOGY.RockMusic.name,
                ONTOLOGY.Microeconomics.name,
                ONTOLOGY.BusinessFinance.name,
                ONTOLOGY.MarketFinance.name,
                ONTOLOGY.Insurance.name,
            ]
        )
        assert true_courses_ == sorted([course_.name for course_ in get_all_courses()])

    @pytest.mark.requests
    def test_thematics_list() -> None:
        """Test thematics list"""
        true_thematics_ = sorted(
            [
                ONTOLOGY.Biology.name,
                ONTOLOGY.History.name,
                ONTOLOGY.Music.name,
                ONTOLOGY.Arts.name,
                ONTOLOGY.Literature.name,
                ONTOLOGY.Astronomy.name,
                ONTOLOGY.Geopolitics.name,
                ONTOLOGY.Economy.name,
                ONTOLOGY.InformationTechnologies.name,
                ONTOLOGY.Finance.name,
            ]
        )
        assert true_thematics_ == sorted(
            [thematic_.name for thematic_ in get_all_thematics()]
        )

    @pytest.mark.requests
    def test_course_modules() -> None:
        """Test course modules"""

        assert pop_music_modules == get_course_modules(ONTOLOGY.PopMusic)

    @pytest.mark.requests
    def test_course_thematic() -> None:
        """Test course thematic"""
        assert [ONTOLOGY.Music] == get_course_thematics(ONTOLOGY.PopMusic)

    @pytest.mark.requests
    def test_course_prerequisites() -> None:
        """Test course prerequisites"""
        assert [
            ONTOLOGY.PopMusicPresentation,
            ONTOLOGY.PopMusicOrigin,
            ONTOLOGY.PopMusic2000,
        ] == get_course_prerequisites(ONTOLOGY.RockMusic)

    @pytest.mark.requests
    def test_module_prerequisites() -> None:
        """Test module prerequisites"""
        assert [ONTOLOGY.PopMusicPresentation] == get_module_prerequisites(
            ONTOLOGY.PopMusicFamousArtists
        )

    @pytest.mark.requests
    def test_module_knowledge() -> None:
        """Test module knowledge"""
        assert sorted(
            [
                ONTOLOGY.In50sRocknRollDominates.name,
                ONTOLOGY.ElvisPresleyFamousRocknRollArtist.name,
                ONTOLOGY.JailhouseRockIsFromElvisPresley.name,
                ONTOLOGY.JailhouseRockPublishedIn1958.name,
                ONTOLOGY.InThe1950sRocknRollSubdivision.name,
                ONTOLOGY.RocknRollSubdivisionBranches.name,
                ONTOLOGY.BluesNotInSubdivision.name,
                ONTOLOGY.RockFaithfulToTheBlues.name,
            ]
        ) == sorted(
            [ele.name for ele in get_module_knowledge(ONTOLOGY.RockNRollPresentation)]
        )

    @pytest.mark.requests
    def test_course_knowledge() -> None:
        """Test course knowledge"""
        assert (
            sorted(
                [
                    ONTOLOGY.FirstApparitionOfPopTerm.name,
                    ONTOLOGY.OriginCountryOfPopTerm.name,
                    ONTOLOGY.TermDevelopmentAmongYoung.name,
                    ONTOLOGY.Int50sPopDoesntDesignAMusicalStyle.name,
                    ONTOLOGY.In50sRocknRollDominates.name,
                    ONTOLOGY.ElvisPresleyFamousRocknRollArtist.name,
                    ONTOLOGY.JailhouseRockIsFromElvisPresley.name,
                    ONTOLOGY.JailhouseRockPublishedIn1958.name,
                    ONTOLOGY.InThe1950sRocknRollSubdivision.name,
                    ONTOLOGY.RocknRollSubdivisionBranches.name,
                    ONTOLOGY.BluesNotInSubdivision.name,
                    ONTOLOGY.RockFaithfulToTheBlues.name,
                    ONTOLOGY.YesterdayIsConsideredFirstPopMusic.name,
                    ONTOLOGY.YesterdayPublishedIn1965InTheUK.name,
                    ONTOLOGY.BeatlesFirstPopMusicGroup.name,
                    ONTOLOGY.BeatlesIsAEnglishGroup.name,
                    ONTOLOGY.BeatlesFormedInLiverpool.name,
                    ONTOLOGY.BeatlesOneOfMostPopular.name,
                    ONTOLOGY.MembersAreJohnLennonPaulMcCartneyGeorgeHarrisonRingoStarr.name,
                    ONTOLOGY.JohnLennonFounder.name,
                    ONTOLOGY.BeatlesCreatedIn1957.name,
                    ONTOLOGY.RingoStarrLastMember.name,
                    ONTOLOGY.PopTurnedToLighterThematics.name,
                    ONTOLOGY.PopMusicStructuresAreSimple.name,
                    ONTOLOGY.PopMusicMelodiesStayInMind.name,
                    ONTOLOGY.PopMusicsAreShort.name,
                    ONTOLOGY.MadonnaSoldMostDisks.name,
                    ONTOLOGY.PopMusicHighlightsMusicians.name,
                    ONTOLOGY.BubbleGumPopIsSubgenreOfPop.name,
                    ONTOLOGY.BubblegumPopCreatedForTeenagers.name,
                    ONTOLOGY.BubblegumPopExploitedBysBrands.name,
                    ONTOLOGY.ArchiesSugarIsBubblegumPop.name,
                    ONTOLOGY.BubblegumPopBecauseOfTeensBubblegum.name,
                    ONTOLOGY.PopBaroqueIsSubgenreOfPop.name,
                    ONTOLOGY.PopBaroqueMixesClassicalBaroqueAndPop.name,
                    ONTOLOGY.PopBaroqueUsesInstrumentsOfClassicalMusique.name,
                    ONTOLOGY.WouldntItBeNiceIsPopBaroque.name,
                    ONTOLOGY.WouldntItBeNiceContainsPiano.name,
                    ONTOLOGY.WouldntItBeNiceFromBeachBoys.name,
                    ONTOLOGY.CountryPopIsSubgenreOfPop.name,
                    ONTOLOGY.PopCountryDevelopedForLargerAudienceByCountryMusicians.name,
                    ONTOLOGY.IconicInstrumentOfCountryIsHarmonica.name,
                    ONTOLOGY.IllAlwaysLoveYouIsPopCountry.name,
                    ONTOLOGY.IllAlwaysLoveYouFromDollyParton.name,
                    ONTOLOGY.TaylorsSwiftContemporaryArtistOfPopCountry.name,
                    ONTOLOGY.SynthetizerAppearedInThe80s.name,
                    ONTOLOGY.SynthetizerHadImportantImpactOnAllMusicStyles.name,
                    ONTOLOGY.DancePopIsSubgenreOfPop.name,
                    ONTOLOGY.DancePopAppearedWithSynthetizers.name,
                    ONTOLOGY.DancePopHasQuickTempo.name,
                    ONTOLOGY.DancePopHasCatchyMusic.name,
                    ONTOLOGY.DancePopEmphesizesOnVideoClips.name,
                    ONTOLOGY.MichaelJacksonConsideredKingOfPop.name,
                    ONTOLOGY.MichealJacksonArtistTheMostSuccessful.name,
                    ONTOLOGY.BillieJeanIsFromMichealJackson.name,
                    ONTOLOGY.ThrillerIsMJsMostSoldAlbum.name,
                    ONTOLOGY.ThrillerMostSoldAlbum.name,
                    ONTOLOGY.ThrillerSold66MExamplarsIn1982.name,
                    ONTOLOGY.MadonnaQueenOfPop.name,
                    ONTOLOGY.MadonnaWasDanceBefore.name,
                    ONTOLOGY.MadonnaDidIconicDancesInClips.name,
                    ONTOLOGY.ChoregraphyImportantForDancePop.name,
                    ONTOLOGY.DancePopIsStillVeryPopular.name,
                    ONTOLOGY.BoysBandsAreTrendyInThe90s.name,
                    ONTOLOGY.BoysBandsGroupHandsomeBoysAndGirls.name,
                    ONTOLOGY.MostFamousGrilsBandSpiceGirl.name,
                    ONTOLOGY.MostFamousMusicOfSpiceGirlsIsWannabe.name,
                    ONTOLOGY.WannabeRankedTopIn37Countries.name,
                    ONTOLOGY.WannabeSoldMoreThan7MCopies.name,
                    ONTOLOGY.BGGroupsWereFormedByProducersForCommercialPurposes.name,
                    ONTOLOGY.BritneySpearsIsConsideredPrincessOfPop.name,
                    ONTOLOGY.BritneySpearsSoldMostDisksInThe2000.name,
                    ONTOLOGY.BritneySpearsSoldMoreThan200MDisksIn2000.name,
                    ONTOLOGY.BabeOneMoreTimeIsFromBS.name,
                    ONTOLOGY.In2000MusicPopDiversisifesAgain.name,
                    ONTOLOGY.BritPopSubgenreOfPop.name,
                    ONTOLOGY.BritPopComesCloserToRockAgain.name,
                    ONTOLOGY.BritPopWasBornInEngland.name,
                    ONTOLOGY.BritPopIsInspiredBy60sRock.name,
                    ONTOLOGY.OasisIsABritPopGroup.name,
                    ONTOLOGY.RihannaGetsCloserToRnb.name,
                    ONTOLOGY.JayZGetsCloserToHipHop.name,
                    ONTOLOGY.HipHopContainsRappedParts.name,
                    ONTOLOGY.LadyGagasMusicIsMoreElectronic.name,
                    ONTOLOGY.LadyGagasMusicIsNewWave.name,
                    ONTOLOGY.LadyGagasMusicHasSmoothedSoundEnvironment.name,
                ]
            )
            == sorted([ele.name for ele in get_course_knowledge(ONTOLOGY.PopMusic)])
        )

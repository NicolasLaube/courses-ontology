"""Thematics instances"""
from owlready2 import locstr

from src.builder import ONTOLOGY
from src.construction.micro_learning.classes import Thematic

with ONTOLOGY:
    biology = Thematic("Biology")
    history = Thematic("History")
    music = Thematic("Music")
    arts = Thematic("Arts")
    literature = Thematic("Literature")
    astronomy = Thematic("Astronomy")
    geopolitic = Thematic("Geopolitics")
    information_technologies = Thematic("InformationTechnologies")
    economy = Thematic("Economy")
    finance = Thematic("Finance")

    economy.label = [
        locstr("L'économie", "fr"),
        locstr("The economy", "en"),
        locstr("Die Wirtschaft", "de"),
        locstr("Economia", "es"),
    ]

    finance.label = [
        locstr("La finance", "fr"),
        locstr("Finance", "en"),
        locstr("Finanzen", "de"),
        locstr("Finanzas", "es"),
    ]

    geopolitic.label = [
        locstr("La géopolitique", "fr"),
        locstr("Geopolitics", "en"),
        locstr("Geopolitik", "de"),
        locstr("Geopolítica", "es"),
    ]

    astronomy.label = [
        locstr("L'astronomie", "fr"),
        locstr("The astronomy", "en"),
        locstr("Die Astronomie", "de"),
        locstr("Astronomía", "es"),
    ]

    biology.label = [
        locstr("Biologie", "fr"),
        locstr("Biology", "en"),
        locstr("Biologie", "de"),
        locstr("Biologia", "es"),
    ]

    history.label = [
        locstr("Histoire", "fr"),
        locstr("History", "en"),
        locstr("Geschichte", "de"),
        locstr("Historia", "es"),
    ]

    music.label = [
        locstr("La musique", "fr"),
        locstr("The music", "en"),
        locstr("Die Musik", "de"),
        locstr("Musica", "es"),
    ]

    arts.label = [
        locstr("Les arts", "fr"),
        locstr("The arts", "en"),
        locstr("Die Künste", "de"),
        locstr("Las artes", "es"),
    ]

    literature.label = [
        locstr("La littérature", "fr"),
        locstr("The Litterature", "en"),
        locstr("Die Literatur", "de"),
        locstr("La literatura", "es"),
    ]

    information_technologies.label = [
        locstr("Sciences de l'information", "fr"),
        locstr("Information technologies", "en"),
        locstr("Informationstechnologien", "de"),
        locstr("Tecnologías de la información", "es"),
    ]

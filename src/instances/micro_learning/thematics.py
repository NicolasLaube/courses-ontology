"""Thematics instances"""
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

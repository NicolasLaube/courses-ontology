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
    economy = Thematic("Economy")
